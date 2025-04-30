import "../css/MovieCard.css"
import { useMovieContext } from "../contexts/MovieContext"
import axios from 'axios';


function MovieCard({movie}) {
    const {isFavorite, addToFavorites, removeFromFavorites, userId} = useMovieContext()
    const favorite = isFavorite(movie.id)

    function onFavoriteClick(e) {
        e.preventDefault()
        e.stopPropagation(); // Prevent card click tracking when heart is clicked
        if (favorite) removeFromFavorites(movie.id)
        else addToFavorites(movie)
    }
    // Track movie card click
    function trackClick() {
        console.log('clicked')
        axios.post("http://localhost:8081/api/clicks/track", {
            movieId: movie.id,
            userId: userId,
            browser: navigator.userAgent,
            deviceType: /Mobi|Android/i.test(navigator.userAgent) ? "Mobile" : "Desktop"
          })
          .then(() => {
            console.log(`Click tracked for movie: ${movie.title}`);
          })
          .catch(err => {
            console.error("Error sending click event:", err);
          });
    }

    return <div className="movie-card" onClick = {trackClick}>
        <div className="movie-poster">
            <img src={`https://image.tmdb.org/t/p/w500${movie.poster_path}`} alt={movie.title} />
            <div className="movie-overlay">
                <button className={`favorite-btn ${favorite ? "active" : ""}`} onClick={onFavoriteClick}>
                    ♥
                </button>
            </div>
        </div>
        <div className="movie-info">
            <h3>{movie.title}</h3>
            <p>{movie.release_date?.split("-")[0]}</p>
        </div>
    </div>
}

export default MovieCard