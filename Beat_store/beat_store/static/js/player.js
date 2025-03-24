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
    const csrfToken = document.querySelector('meta[name="csrf-token"]')?.content || null;

    if (!csrfToken) {
        console.error('CSRF-токен не найден. Убедитесь, что он добавлен в <meta> в head.');
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

        playlist = [];
        document.querySelectorAll('.play-button').forEach((button) => {
            const songItem = button.closest('.song-item');
            const authorElement = songItem.querySelector('.song-author-link') || songItem.querySelector('.song-author');
            const author = authorElement ? authorElement.textContent.trim() : 'Неизвестен';
            const songId = button.getAttribute('data-song-id');
            const likeButton = songItem.querySelector('.like-button');
            playlist.push({
                id: songId,
                url: button.getAttribute('data-song-url'),
                title: button.getAttribute('data-song-title'),
                author: author,
                likes: likeButton ? parseInt(likeButton.dataset.likes) || 0 : 0
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
        if (likeButtonPlayer) {
            likeButtonPlayer.addEventListener('click', handlePlayerLikeClick);
        } else {
            console.error('Кнопка like-button-player не найдена');
        }

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
                savePlayerState();
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
        fetch(`/play-song/${songId}/`, {
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
                const playCountElement = document.getElementById(`plays-count-${songId}`);
                if (playCountElement) playCountElement.innerHTML = `<i class="bi bi-play-fill"></i> ${data.total_likes}`;
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
            this.dataset.likes = data.total_likes;
            if (songId === currentSongId) {
                likeButtonPlayer.classList.toggle('liked', data.liked);
                likeButtonPlayer.dataset.likes = data.total_likes;
                playlist[currentIndex].likes = data.total_likes;
            }
        });
    }

    function handlePlayerLikeClick() {
        if (!currentSongId) {
            console.warn('Нет текущей песни для лайка');
            return;
        }
        console.log('Нажата кнопка лайка в плеере для songId:', currentSongId);
        toggleLike(currentSongId, likeButtonPlayer, (data) => {
            console.log('Ответ от сервера:', data);
            const songLikeButton = document.querySelector(`[data-song-id="${currentSongId}"] .like-button`);
            if (songLikeButton) {
                songLikeButton.classList.toggle('liked', data.liked);
                songLikeButton.dataset.likes = data.total_likes;
                console.log('Обновлена кнопка на странице:', songLikeButton);
            }
            likeButtonPlayer.classList.toggle('liked', data.liked);
            likeButtonPlayer.dataset.likes = data.total_likes;
            playlist[currentIndex].likes = data.total_likes;
            console.log('Обновлена кнопка в плеере:', likeButtonPlayer);
            savePlayerState();
        });
    }

    function handleBuyClick() {
        const songId = this.closest('.song-item').getAttribute('data-song-id');
        alert('Функция покупки пока в разработке!');
    }

    function toggleLike(songId, button, callback) {
        console.log('Отправка запроса на /like/', songId);
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
                console.log('Успешный ответ:', data);
                button.classList.toggle('liked', data.liked);
                button.dataset.likes = data.total_likes;
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
        const isLiked = likeButton?.classList.contains('liked') || false;
        const likesCount = likeButton ? parseInt(likeButton.dataset.likes) || 0 : 0;
        likeButtonPlayer.classList.toggle('liked', isLiked);
        likeButtonPlayer.dataset.likes = likesCount;
        if (currentIndex >= 0 && currentIndex < playlist.length) {
            playlist[currentIndex].likes = likesCount;
        }
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
            likes: parseInt(likeButtonPlayer.dataset.likes) || playlist[currentIndex].likes || 0,
            liked: likeButtonPlayer.classList.contains('liked')
        };
        localStorage.setItem('currentSong', JSON.stringify(songData));
    }

    function restorePlayerState() {
        const savedSong = JSON.parse(localStorage.getItem('currentSong'));
        if (!savedSong || !savedSong.url) return;

        currentIndex = playlist.findIndex((song) => song.id === savedSong.id);
        if (currentIndex === -1) {
            audioSource.src = savedSong.url;
            audioPlayer.load();
            audioPlayer.currentTime = savedSong.time || 0;
            audioPlayer.volume = savedSong.volume || 0.5;
            volumeSlider.value = savedSong.volume || 0.5;
            currentSongDisplay.textContent = `${savedSong.title} - ${savedSong.author || 'Неизвестен'}`;
            currentSongId = savedSong.id;
            likeButtonPlayer.classList.toggle('liked', savedSong.liked || false);
            likeButtonPlayer.dataset.likes = savedSong.likes || 0;
            if (savedSong.isPlaying) {
                audioPlayer.play().catch((err) => console.error('Ошибка воспроизведения:', err));
            }
        } else {
            playSongByIndex(currentIndex);
            audioPlayer.currentTime = savedSong.time || 0;
            if (!savedSong.isPlaying) audioPlayer.pause();
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
        updatePlayPauseIcon(false);
    }

    return { init };
})();