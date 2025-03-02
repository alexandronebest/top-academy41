const Player = (function() {
    let audioPlayer, audioSource, currentSongDisplay, likeButtonPlayer, playPauseButton, volumeSlider;
    let currentSongId = null;
    const csrfToken = document.querySelector('meta[name="csrf-token"]')?.content || 
                     document.querySelector('input[name="csrfmiddlewaretoken"]')?.value;

    function init() {
        audioPlayer = document.getElementById('audio-player');
        audioSource = document.getElementById('audio-source');
        currentSongDisplay = document.getElementById('current-song');
        likeButtonPlayer = document.getElementById('like-button-player');
        playPauseButton = document.getElementById('play-pause-button');
        volumeSlider = document.getElementById('volume-slider');

        if (!audioPlayer || !audioSource || !currentSongDisplay || !likeButtonPlayer) {
            console.error('One or more required player elements are missing');
            return;
        }

        if (volumeSlider) audioPlayer.volume = volumeSlider.value;
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
        audioPlayer.addEventListener('play', savePlayerState);
        audioPlayer.addEventListener('pause', savePlayerState);
        audioPlayer.addEventListener('timeupdate', savePlayerState);
        audioPlayer.addEventListener('ended', handleSongEnd);
        likeButtonPlayer.addEventListener('click', handlePlayerLikeClick);
        if (playPauseButton) {
            playPauseButton.addEventListener('click', () => {
                if (audioPlayer.paused) audioPlayer.play();
                else audioPlayer.pause();
            });
        }
        if (volumeSlider) {
            volumeSlider.addEventListener('input', () => {
                audioPlayer.volume = volumeSlider.value;
            });
        }
        window.addEventListener('load', restorePlayerState);
    }

    function handlePlayClick() {
        const songUrl = this.getAttribute('data-song-url');
        const songTitle = this.getAttribute('data-song-title');
        const songId = this.getAttribute('data-song-id');
        const songContainer = this.closest('[data-song-id]');
        let authorName;

        const authorLink = songContainer.querySelector('.song-author-link');
        if (authorLink) {
            authorName = authorLink.textContent.trim();
        } else {
            const textContent = songContainer.childNodes[0].textContent.trim();
            const parts = textContent.split(' - ');
            authorName = parts.length > 1 ? parts[1].trim() : 'Unknown';
        }

        const playIcon = this.querySelector('i');

        if (currentSongId === songId) {
            if (audioPlayer.paused) {
                audioPlayer.play().catch(err => console.error("Playback error:", err));
                playIcon.classList.replace('bi-play-fill', 'bi-pause-fill');
            } else {
                audioPlayer.pause();
                playIcon.classList.replace('bi-pause-fill', 'bi-play-fill');
            }
        } else {
            resetPlayButtons();
            audioSource.src = songUrl;
            audioPlayer.load();
            audioPlayer.play().catch(err => console.error("Playback error:", err));
            currentSongDisplay.textContent = `${songTitle} - ${authorName}`;
            currentSongId = songId;
            playIcon.classList.replace('bi-play-fill', 'bi-pause-fill');
            if (songContainer) updatePlayerLikeState(songContainer);
        }
        savePlayerState();
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
        const parts = currentSongDisplay.textContent.split(' - ');
        const songData = {
            id: currentSongId,
            url: audioSource.src,
            title: parts[0].trim(),
            author: parts.length > 1 ? parts[1].trim() : 'Unknown',
            time: audioPlayer.currentTime,
            isPlaying: !audioPlayer.paused
        };
        localStorage.setItem('currentSong', JSON.stringify(songData));
    }

    function restorePlayerState() {
        const savedSong = JSON.parse(localStorage.getItem('currentSong'));
        if (savedSong && savedSong.url) {
            audioSource.src = savedSong.url;
            audioPlayer.load();
            audioPlayer.currentTime = savedSong.time || 0;
            currentSongDisplay.textContent = `${savedSong.title} - ${savedSong.author}`;
            currentSongId = savedSong.id;
            if (savedSong.isPlaying) {
                audioPlayer.play().catch(err => console.error("Playback error:", err));
                if (playPauseButton) {
                    playPauseButton.querySelector('i').classList.replace('bi-play-fill', 'bi-pause-fill');
                }
            }
            const songContainer = document.querySelector(`[data-song-id="${currentSongId}"]`);
            if (songContainer) updatePlayerLikeState(songContainer);
        }
    }

    function handleSongEnd() {
        resetPlayButtons();
        currentSongId = null;
        localStorage.removeItem('currentSong');
        currentSongDisplay.textContent = 'Выберите песню для воспроизведения';
        likeButtonPlayer.classList.remove('liked');
        if (playPauseButton) {
            playPauseButton.querySelector('i').classList.replace('bi-pause-fill', 'bi-play-fill');
        }
    }

    return { init: init };
})();