const Player = (function () {
    let audioPlayer,
        audioSource,
        currentSongDisplay,
        likeButtonPlayer,
        playPauseButton,
        volumeSlider,
        progressBar,
        prevButton,
        nextButton,
        muteButton,
        currentTimeDisplay,
        totalTimeDisplay,
        songPriceElement;

    let currentSongId = null;
    let playlist = [];
    let currentIndex = -1;
    let previousVolume = 0.5;
    let hasPlayed = false;

    const csrfToken = document.querySelector('meta[name="csrf-token"]')?.content || '';

    function init(songsData = []) {
        playlist = songsData.map(song => ({
            id: song.id,
            url: song.path,
            title: song.title,
            author: song.author,
            likes: song.total_likes || 0,
            price: parseFloat(song.price) || 0,
            plays: song.total_plays || 0
        }));

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
        songPriceElement = document.getElementById('song-price');

        if (!audioPlayer || !audioSource || !currentSongDisplay) {
            console.error('Необходимые элементы плеера не найдены');
            return;
        }

        audioPlayer.volume = localStorage.getItem('volume') || 0.5;
        volumeSlider.value = audioPlayer.volume;
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

        audioPlayer.addEventListener('play', () => {
            updatePlayPauseIcon(true);
            updateSongIcon(currentSongId, true);
            if (!hasPlayed) {
                incrementPlayCount(currentSongId);
                hasPlayed = true;
            }
            savePlayerState();
        });
        audioPlayer.addEventListener('pause', () => {
            updatePlayPauseIcon(false);
            updateSongIcon(currentSongId, false);
            savePlayerState();
        });
        audioPlayer.addEventListener('timeupdate', () => {
            progressBar.value = audioPlayer.currentTime / audioPlayer.duration || 0;
            updateTimeDisplay();
        });
        audioPlayer.addEventListener('loadedmetadata', updateTimeDisplay);
        audioPlayer.addEventListener('ended', playNextSong);
        audioPlayer.addEventListener('error', e => {
            console.error('Ошибка аудио:', e);
            playNextSong();
        });

        likeButtonPlayer.addEventListener('click', handlePlayerLikeClick);
        playPauseButton.addEventListener('click', togglePlayPause);
        prevButton.addEventListener('click', playPreviousSong);
        nextButton.addEventListener('click', playNextSong);
        volumeSlider.addEventListener('input', () => {
            audioPlayer.volume = volumeSlider.value;
            updateMuteIcon();
            localStorage.setItem('volume', volumeSlider.value);
        });
        muteButton.addEventListener('click', toggleMute);
        progressBar.addEventListener('input', () => {
            audioPlayer.currentTime = progressBar.value * audioPlayer.duration;
            savePlayerState();
        });

        window.addEventListener('load', restorePlayerState);
        document.addEventListener('keydown', handleKeyboardControls);
    }

    function handlePlayClick() {
        const songId = this.getAttribute('data-song-id');
        const songUrl = this.getAttribute('data-song-url');
        const songTitle = this.getAttribute('data-song-title');

        if (currentSongId === songId) {
            togglePlayPause();
        } else {
            playSong(songId, songUrl, songTitle);
        }
    }

    function playSong(songId, songUrl, songTitle) {
        const songIndex = playlist.findIndex(song => song.id === parseInt(songId, 10));
        resetPlayButtons();
        audioSource.src = songUrl;
        audioPlayer.load();
        audioPlayer.play()
            .then(() => {
                currentSongDisplay.textContent = songTitle;
                currentSongId = songId;
                currentIndex = songIndex !== -1 ? songIndex : currentIndex;
                hasPlayed = false;
                updatePlayPauseIcon(true);
                updateSongIcon(songId, true);
                updatePlayerLikeState(songId);
                updateSongPrice(songIndex !== -1 ? playlist[songIndex].price : 0);
                savePlayerState();
            })
            .catch(err => {
                console.error('Ошибка воспроизведения:', err);
                playNextSong();
            });
    }

    function updateSongPrice(price) {
        songPriceElement.textContent = `₽${price.toFixed(2)}`;
    }

    function incrementPlayCount(songId) {
        fetch(`/play-song/${songId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json',
            },
        })
            .then(response => response.ok ? response.json() : Promise.reject(response.status))
            .then(data => {
                const playCountElement = document.getElementById(`plays-count-${songId}`);
                if (playCountElement) playCountElement.innerHTML = `<i class="bi bi-play-fill"></i> ${data.total_plays}`;
                if (currentIndex !== -1) playlist[currentIndex].plays = data.total_plays;
            })
            .catch(error => console.error('Ошибка при увеличении счётчика:', error));
    }

    function playNextSong() {
        if (currentIndex < playlist.length - 1 && currentIndex !== -1) {
            const nextSong = playlist[currentIndex + 1];
            playSong(nextSong.id, nextSong.url, `${nextSong.title} - ${nextSong.author || 'Неизвестен'}`);
        } else {
            handleSongEnd();
        }
    }

    function playPreviousSong() {
        if (currentIndex > 0 && currentIndex !== -1) {
            const prevSong = playlist[currentIndex - 1];
            playSong(prevSong.id, prevSong.url, `${prevSong.title} - ${prevSong.author || 'Неизвестен'}`);
        }
    }

    function togglePlayPause() {
        if (!currentSongId) return;

        if (audioPlayer.paused) {
            audioPlayer.play()
                .then(() => updatePlayPauseIcon(true))
                .catch(err => console.error('Ошибка воспроизведения:', err));
        } else {
            audioPlayer.pause();
        }
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

    function updateSongIcon(songId, isPlaying) {
        const playIcon = document.querySelector(`[data-song-id="${songId}"] .play-button i`);
        if (playIcon) {
            playIcon.classList.toggle('bi-play-fill', !isPlaying);
            playIcon.classList.toggle('bi-pause-fill', isPlaying);
        }
    }

    function updateTimeDisplay() {
        currentTimeDisplay.textContent = formatTime(audioPlayer.currentTime);
        totalTimeDisplay.textContent = formatTime(audioPlayer.duration);
    }

    function formatTime(seconds) {
        if (isNaN(seconds)) return '0:00';
        const minutes = Math.floor(seconds / 60);
        const secs = Math.floor(seconds % 60);
        return `${minutes}:${secs < 10 ? '0' : ''}${secs}`;
    }

    function handleKeyboardControls(e) {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
        if (e.key === 'ArrowRight') playNextSong();
        if (e.key === 'ArrowLeft') playPreviousSong();
        if (e.key === ' ') {
            e.preventDefault();
            togglePlayPause();
        }
    }

    function handleLikeClick() {
        const songId = this.getAttribute('data-song-id');
        toggleLike(songId, this, data => {
            this.dataset.likes = data.total_likes;
            if (songId === currentSongId) {
                likeButtonPlayer.classList.toggle('liked', data.liked);
                likeButtonPlayer.dataset.likes = data.total_likes;
                if (currentIndex !== -1) playlist[currentIndex].likes = data.total_likes;
            }
        });
    }

    function handlePlayerLikeClick() {
        if (!currentSongId) return;
        toggleLike(currentSongId, likeButtonPlayer, data => {
            const songLikeButton = document.querySelector(`[data-song-id="${currentSongId}"] .like-button`);
            if (songLikeButton) {
                songLikeButton.classList.toggle('liked', data.liked);
                songLikeButton.dataset.likes = data.total_likes;
            }
            likeButtonPlayer.dataset.likes = data.total_likes;
            if (currentIndex !== -1) playlist[currentIndex].likes = data.total_likes;
        });
    }

    function toggleLike(songId, button, callback) {
        fetch(`/like/${songId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json',
            },
        })
            .then(response => response.ok ? response.json() : Promise.reject(response.status))
            .then(data => {
                button.classList.toggle('liked', data.liked);
                button.dataset.likes = data.total_likes;
                callback(data);
            })
            .catch(error => console.error('Ошибка при лайке:', error));
    }

    function resetPlayButtons() {
        document.querySelectorAll('.play-button i').forEach(icon => {
            icon.classList.replace('bi-pause-fill', 'bi-play-fill');
        });
    }

    function updatePlayerLikeState(songId) {
        const songContainer = document.querySelector(`[data-song-id="${songId}"]`);
        const likeButton = songContainer?.querySelector('.like-button');
        const isLiked = likeButton?.classList.contains('liked') || false;
        const likesCount = likeButton ? parseInt(likeButton.dataset.likes) || 0 : 0;
        likeButtonPlayer.classList.toggle('liked', isLiked);
        likeButtonPlayer.dataset.likes = likesCount;
    }

    function savePlayerState() {
        if (!currentSongId) return;
        const songData = {
            id: currentSongId,
            url: audioSource.src,
            title: currentSongDisplay.textContent.split(' - ')[0],
            author: currentSongDisplay.textContent.split(' - ')[1] || 'Неизвестен',
            time: audioPlayer.currentTime,
            isPlaying: !audioPlayer.paused,
            volume: audioPlayer.volume,
            likes: parseInt(likeButtonPlayer.dataset.likes) || 0,
            liked: likeButtonPlayer.classList.contains('liked'),
            price: parseFloat(songPriceElement.textContent.replace('₽', '')) || 0
        };
        localStorage.setItem('currentSong', JSON.stringify(songData));
    }

    function restorePlayerState() {
        const savedSong = JSON.parse(localStorage.getItem('currentSong'));
        if (!savedSong || !savedSong.url) return;

        const songIndex = playlist.findIndex(song => song.id === savedSong.id);
        audioSource.src = savedSong.url;
        audioPlayer.load();
        audioPlayer.currentTime = savedSong.time || 0;
        audioPlayer.volume = savedSong.volume || 0.5;
        volumeSlider.value = savedSong.volume || 0.5;
        currentSongDisplay.textContent = `${savedSong.title} - ${savedSong.author}`;
        currentSongId = savedSong.id;
        currentIndex = songIndex !== -1 ? songIndex : -1;
        likeButtonPlayer.classList.toggle('liked', savedSong.liked || false);
        likeButtonPlayer.dataset.likes = savedSong.likes || 0;
        updateSongPrice(savedSong.price || 0);
        if (savedSong.isPlaying) {
            audioPlayer.play()
                .then(() => updatePlayPauseIcon(true))
                .catch(err => console.error('Ошибка воспроизведения:', err));
        } else {
            updatePlayPauseIcon(false);
        }
        updateMuteIcon();
    }

    function handleSongEnd() {
        resetPlayButtons();
        currentSongId = null;
        currentIndex = -1;
        localStorage.removeItem('currentSong');
        currentSongDisplay.textContent = 'Выберите песню для воспроизведения';
        likeButtonPlayer.classList.remove('liked');
        likeButtonPlayer.dataset.likes = '0';
        updateSongPrice(0);
        updatePlayPauseIcon(false);
    }

    return { init };
})();