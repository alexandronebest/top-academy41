const Player = (function() {
    let audioPlayer, audioSource, currentSongDisplay, likeButtonPlayer, playPauseButton, volumeSlider, progressBar, prevButton, nextButton, muteButton, currentTimeDisplay, totalTimeDisplay;
    let currentSongId = null;
    let playlist = [];
    let currentIndex = -1;
    let previousVolume = 0.5;
    const csrfToken = document.querySelector('meta[name="csrf-token"]')?.content || 
                     document.querySelector('input[name="csrfmiddlewaretoken"]')?.value;

    function init() {
        audioPlayer = document.getElementById('audio-player');
        audioSource = document.getElementById('audio-source');
        currentSongDisplay = document.getElementById('current-song');
        likeButtonPlayer = document.getElementById('like-button-player');
        playPauseButton = document.getElementById('play-pause-button');
        volumeSlider = document.getElementById('volume-slider');
        progressBar = document.getElementById('progress-bar');
        prevButton = document.getElementById('prev-button');
        nextButton = document.getElementById('next-button');
        muteButton = document.getElementById('mute-button');
        currentTimeDisplay = document.getElementById('current-time');
        totalTimeDisplay = document.getElementById('total-time');

        if (!audioPlayer || !audioSource || !currentSongDisplay || !likeButtonPlayer) {
            console.error('One or more required player elements are missing');
            return;
        }

        document.querySelectorAll('.play-button').forEach(button => {
            // console.log(button)
            console.log(button.closest('.song-item').querySelector('.song-author-link'))
            playlist.push({
                id: button.getAttribute('data-song-id'),
                url: button.getAttribute('data-song-url'),
                title: button.getAttribute('data-song-title'),
                author: button.closest('.song-item').querySelector('.song-author-link')?.textContent.trim() || 'Unknown'
            });
        });

        audioPlayer.volume = volumeSlider?.value || 0.5;
        setupEventListeners();
        restorePlayerState();
    }

    function setupEventListeners() {
        document.querySelectorAll('.play-button').forEach(button => {
            button.addEventListener('click', handlePlayClick);
        });
        document.querySelectorAll('.like-button').forEach(button => {
            button.addEventListener('click', handleLikeClick);
        });
        document.querySelectorAll('.buy-button').forEach(button => {
            button.addEventListener('click', handleBuyClick);
        });

        audioPlayer.addEventListener('play', () => {
            savePlayerState();
            updatePlayPauseIcon(true);
            const playIcon = document.querySelector(`[data-song-id="${currentSongId}"] .play-button i`);
            if (playIcon) playIcon.classList.replace('bi-play-fill', 'bi-pause-fill');
        });
        audioPlayer.addEventListener('pause', () => {
            savePlayerState();
            updatePlayPauseIcon(false);
            const playIcon = document.querySelector(`[data-song-id="${currentSongId}"] .play-button i`);
            if (playIcon) playIcon.classList.replace('bi-pause-fill', 'bi-play-fill');
        });
        audioPlayer.addEventListener('timeupdate', () => {
            savePlayerState();
            if (progressBar) progressBar.value = audioPlayer.currentTime / audioPlayer.duration || 0;
            updateTimeDisplay();
        });
        audioPlayer.addEventListener('loadedmetadata', () => {
            updateTimeDisplay();
        });
        audioPlayer.addEventListener('ended', playNextSong);
        likeButtonPlayer.addEventListener('click', handlePlayerLikeClick);

        if (playPauseButton) playPauseButton.addEventListener('click', togglePlayPause);
        if (prevButton) prevButton.addEventListener('click', playPreviousSong);
        if (nextButton) nextButton.addEventListener('click', playNextSong);
        
        if (volumeSlider) {
            volumeSlider.addEventListener('input', () => {
                audioPlayer.volume = volumeSlider.value;
                updateMuteIcon();
                localStorage.setItem('volume', volumeSlider.value);
            });
        }
        if (muteButton) {
            muteButton.addEventListener('click', toggleMute);
        }
        if (progressBar) {
            progressBar.addEventListener('input', () => {
                audioPlayer.currentTime = progressBar.value * audioPlayer.duration;
            });
        }

        window.addEventListener('load', restorePlayerState);
        document.addEventListener('keydown', handleKeyboardControls);
    }

    function handlePlayClick() {
        const songId = this.getAttribute('data-song-id');
        const clickedIndex = playlist.findIndex(song => song.id === songId);

        if (currentSongId === songId && currentIndex === clickedIndex) {
            if (audioPlayer.paused) {
                audioPlayer.play().catch(err => console.error("Playback error:", err));
            } else {
                audioPlayer.pause();
            }
        } else {
            currentIndex = clickedIndex;
            playSongByIndex(currentIndex);
        }
    }

    function playSongByIndex(index) {
        if (index < 0 || index >= playlist.length) return;
        const song = playlist[index];
        const playIcon = document.querySelector(`[data-song-id="${song.id}"] .play-button i`);

        resetPlayButtons();
        audioSource.src = song.url;
        audioPlayer.load();
        audioPlayer.play().catch(err => console.error("Playback error:", err));
        currentSongDisplay.textContent = `${song.title} - ${song.author}`;
        currentSongId = song.id;
        currentIndex = index;
        if (playIcon) playIcon.classList.replace('bi-play-fill', 'bi-pause-fill');
        const songContainer = document.querySelector(`[data-song-id="${currentSongId}"]`);
        if (songContainer) updatePlayerLikeState(songContainer);
        savePlayerState();
    }

    function playNextSong() {
        if (currentIndex < playlist.length - 1) {
            playSongByIndex(currentIndex + 1);
        } else {
            handleSongEnd();
        }
    }

    function playPreviousSong() {
        if (currentIndex > 0) {
            playSongByIndex(currentIndex - 1);
        }
    }

    function togglePlayPause() {
        if (audioPlayer.paused) audioPlayer.play();
        else audioPlayer.pause();
    }

    function toggleMute() {
        if (audioPlayer.volume > 0) {
            previousVolume = audioPlayer.volume;
            audioPlayer.volume = 0;
            volumeSlider.value = 0;
        } else {
            audioPlayer.volume = previousVolume;
            volumeSlider.value = previousVolume;
        }
        updateMuteIcon();
        localStorage.setItem('volume', audioPlayer.volume);
    }

    function updateMuteIcon() {
        const icon = muteButton.querySelector('i');
        icon.classList.toggle('bi-volume-mute-fill', audioPlayer.volume === 0);
        icon.classList.toggle('bi-volume-up-fill', audioPlayer.volume > 0);
    }

    function updatePlayPauseIcon(isPlaying) {
        const icon = playPauseButton.querySelector('i');
        icon.classList.toggle('bi-play-fill', !isPlaying);
        icon.classList.toggle('bi-pause-fill', isPlaying);
    }

    function updateTimeDisplay() {
        if (currentTimeDisplay) {
            currentTimeDisplay.textContent = formatTime(audioPlayer.currentTime);
        }
        if (totalTimeDisplay) {
            totalTimeDisplay.textContent = formatTime(audioPlayer.duration);
        }
    }

    function formatTime(seconds) {
        if (isNaN(seconds)) return '0:00';
        const minutes = Math.floor(seconds / 60);
        const secs = Math.floor(seconds % 60);
        return `${minutes}:${secs < 10 ? '0' : ''}${secs}`;
    }

    function handleKeyboardControls(e) {
        if (e.key === 'ArrowRight') playNextSong();
        if (e.key === 'ArrowLeft') playPreviousSong();
        if (e.key === ' ') {
            e.preventDefault();
            togglePlayPause();
        }
    }

    function handleLikeClick() {
        const songId = this.getAttribute('data-song-id');
        toggleLike(songId, this, (data) => {
            if (songId === currentSongId) {
                likeButtonPlayer.classList.toggle('liked', data.liked);
            }
        });
    }

    function handlePlayerLikeClick() {
        if (!currentSongId) return;
        toggleLike(currentSongId, this, (data) => {
            const songLikeButton = document.querySelector(`[data-song-id="${currentSongId}"] .like-button`);
            if (songLikeButton) songLikeButton.classList.toggle('liked', data.liked);
        });
    }

    function handleBuyClick() {
        const songId = this.closest('[data-song-id]').getAttribute('data-song-id');
        window.location.href = `/store/buy/${songId}/`;
    }

    function toggleLike(songId, button, callback) {
        fetch(`/like/${songId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (!response.ok) throw new Error('Network response was not ok');
            return response.json();
        })
        .then(data => {
            const countSpan = document.getElementById(`likes-count-${songId}`);
            if (countSpan) countSpan.textContent = data.total_likes;
            button.classList.toggle('liked', data.liked);
            if (callback) callback(data);
        })
        .catch(error => console.error('Error liking song:', error));
    }

    function resetPlayButtons() {
        document.querySelectorAll('.play-button i').forEach(icon => {
            icon.classList.replace('bi-pause-fill', 'bi-play-fill');
        });
    }

    function updatePlayerLikeState(songContainer) {
        const likeButton = songContainer.querySelector('.like-button');
        const isLiked = likeButton && likeButton.classList.contains('liked');
        likeButtonPlayer.classList.toggle('liked', isLiked);
    }

    function savePlayerState() {
        if (!currentSongId) return;
        const songData = {
            id: currentSongId,
            url: audioSource.src,
            title: playlist[currentIndex].title,
            author: playlist[currentIndex].author,
            time: audioPlayer.currentTime,
            isPlaying: !audioPlayer.paused,
            volume: audioPlayer.volume
        };
        localStorage.setItem('currentSong', JSON.stringify(songData));
    }

    function restorePlayerState() {
        const savedSong = JSON.parse(localStorage.getItem('currentSong'));
        if (savedSong && savedSong.url) {
            audioSource.src = savedSong.url;
            audioPlayer.load();
            audioPlayer.currentTime = savedSong.time || 0;
            audioPlayer.volume = savedSong.volume || 0.5;
            volumeSlider.value = savedSong.volume || 0.5;
            currentSongDisplay.textContent = `${savedSong.title} - ${savedSong.author}`;
            currentSongId = savedSong.id;
            currentIndex = playlist.findIndex(song => song.id === savedSong.id);
            if (savedSong.isPlaying) {
                audioPlayer.play().catch(err => console.error("Playback error:", err));
            }
            const songContainer = document.querySelector(`[data-song-id="${currentSongId}"]`);
            if (songContainer) updatePlayerLikeState(songContainer);
            updateMuteIcon();
        }
    }

    function handleSongEnd() {
        resetPlayButtons();
        currentSongId = null;
        currentIndex = -1;
        localStorage.removeItem('currentSong');
        currentSongDisplay.textContent = 'Выберите песню для воспроизведения';
        likeButtonPlayer.classList.remove('liked');
        updatePlayPauseIcon(false);
    }

    return { init };
})();