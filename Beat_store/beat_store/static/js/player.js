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
        totalTimeDisplay;
    let currentSongId = null;
    let playlist = [];
    let currentIndex = -1;
    let previousVolume = 0.5;
    const csrfToken =
        document.querySelector('meta[name="csrf-token"]')?.content ||
        document.querySelector('input[name="csrfmiddlewaretoken"]')?.value || null;

    if (!csrfToken) {
        console.error('CSRF-токен не найден. Добавьте {% csrf_token %} или <input name="csrfmiddlewaretoken"> в шаблон.');
    }

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
            console.error('Не найдены необходимые элементы плеера');
            return;
        }

        // Заполнение плейлиста
        document.querySelectorAll('.play-button').forEach((button) => {
            const songItem = button.closest('.song-item');
            const authorElement = songItem.querySelector('.song-author-link') || songItem.querySelector('.song-author');
            const author = authorElement ? authorElement.textContent.trim() : 'Неизвестен';
            const songId = button.getAttribute('data-song-id');
            console.log(`Добавлена песня в плейлист: ID: ${songId}, Title: ${button.getAttribute('data-song-title')}, Author: ${author}`);
            playlist.push({
                id: songId,
                url: button.getAttribute('data-song-url'),
                title: button.getAttribute('data-song-title'),
                author: author,
            });
        });

        audioPlayer.volume = volumeSlider?.value || 0.5;
        setupEventListeners();
        restorePlayerState();
    }

    function setupEventListeners() {
        document.querySelectorAll('.play-button').forEach((button) => {
            button.addEventListener('click', handlePlayClick);
        });
        document.querySelectorAll('.like-button').forEach((button) => {
            button.addEventListener('click', handleLikeClick);
        });
        document.querySelectorAll('.buy-button').forEach((button) => {
            button.addEventListener('click', handleBuyClick);
        });

        audioPlayer.addEventListener('play', () => {
            savePlayerState();
            updatePlayPauseIcon(true);
            updateSongIcon(currentSongId, true);
        });
        audioPlayer.addEventListener('pause', () => {
            savePlayerState();
            updatePlayPauseIcon(false);
            updateSongIcon(currentSongId, false);
        });
        audioPlayer.addEventListener('timeupdate', () => {
            savePlayerState();
            if (progressBar) progressBar.value = audioPlayer.currentTime / audioPlayer.duration || 0;
            updateTimeDisplay();
        });
        audioPlayer.addEventListener('loadedmetadata', updateTimeDisplay);
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
        if (muteButton) muteButton.addEventListener('click', toggleMute);
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
        const clickedIndex = playlist.findIndex((song) => song.id === songId);

        if (currentSongId === songId && currentIndex === clickedIndex) {
            togglePlayPause();
        } else {
            currentIndex = clickedIndex;
            playSongByIndex(currentIndex);
        }
    }

    function playSongByIndex(index) {
        if (index < 0 || index >= playlist.length) return;
        const song = playlist[index];
        console.log(`Воспроизведение песни: ${song.title}, Автор: ${song.author}, ID: ${song.id}`);
        const playIcon = document.querySelector(`[data-song-id="${song.id}"] .play-button i`);

        resetPlayButtons();
        audioSource.src = song.url;
        audioPlayer.load();
        audioPlayer.play().catch((err) => console.error('Ошибка воспроизведения:', err));
        currentSongDisplay.textContent = `${song.title} - ${song.author || 'Неизвестен'}`;
        currentSongId = song.id;
        currentIndex = index;
        if (playIcon) playIcon.classList.replace('bi-play-fill', 'bi-pause-fill');

        const songContainer = document.querySelector(`[data-song-id="${currentSongId}"]`);
        if (songContainer) updatePlayerLikeState(songContainer);

        incrementPlayCount(song.id);
        savePlayerState();
    }

    function incrementPlayCount(songId) {
        console.log(`Отправка запроса для увеличения total_plays, songId: ${songId}, CSRF-токен: ${csrfToken}`);
        fetch(`/play-song/${songId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json',
            },
        })
            .then((response) => {
                console.log(`Ответ от сервера для songId ${songId}: ${response.status}`);
                if (!response.ok) throw new Error(`Ошибка сети: ${response.status}`);
                return response.json();
            })
            .then((data) => {
                const playCountElement = document.getElementById(`plays-count-${songId}`);
                if (playCountElement) {
                    playCountElement.innerHTML = `<i class="bi bi-play-fill"></i> ${data.total_plays}`;
                    console.log(`Song ${songId} played, total_plays updated to ${data.total_plays}`);
                } else {
                    console.warn(`Элемент с id="plays-count-${songId}" не найден`);
                }
            })
            .catch((error) => console.error('Ошибка при увеличении счетчика:', error));
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
        if (audioPlayer.paused) {
            audioPlayer.play().catch((err) => console.error('Ошибка воспроизведения:', err));
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
        const songId = this.closest('.song-item').getAttribute('data-song-id');
        window.location.href = `/store/buy/${songId}/`;
    }

    function toggleLike(songId, button, callback) {
        console.log(`Отправка запроса на лайк для songId: ${songId}`);
        fetch(`/like/${songId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json',
            },
        })
            .then((response) => {
                if (!response.ok) throw new Error(`Ошибка сети: ${response.status}`);
                return response.json();
            })
            .then((data) => {
                const countSpan = document.getElementById(`likes-count-${songId}`);
                if (countSpan) {
                    countSpan.innerHTML = `<i class="bi bi-heart-fill"></i> ${data.total_likes}`;
                    console.log(`Лайки для songId ${songId} обновлены: ${data.total_likes}`);
                } else {
                    console.warn(`Элемент с id="likes-count-${songId}" не найден`);
                }
                button.classList.toggle('liked', data.liked);
                if (callback) callback(data);
            })
            .catch((error) => console.error('Ошибка при лайке:', error));
    }

    function resetPlayButtons() {
        document.querySelectorAll('.play-button i').forEach((icon) => {
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
            volume: audioPlayer.volume,
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
            currentSongDisplay.textContent = `${savedSong.title} - ${savedSong.author || 'Неизвестен'}`;
            currentSongId = savedSong.id;
            currentIndex = playlist.findIndex((song) => song.id === savedSong.id);
            if (savedSong.isPlaying) {
                audioPlayer.play().catch((err) => console.error('Ошибка воспроизведения:', err));
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