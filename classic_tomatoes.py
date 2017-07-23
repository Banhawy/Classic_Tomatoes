import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head_1 = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Classic Tomatoes</title>

        <!-- Bootstrap 3 -->
        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
        <script src="https://code.jquery.com/jquery-1.10.1.min.js"></script>
        <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
        <style type="text/css" media="screen">
            body { padding-top: 80px; }
            a {
                color: grey;
            }
            #trailer .modal-dialog {
                margin-top: 200px;
                width: 640px;
                height: 480px;
            }
            .hanging-close {
                position: absolute;
                top: -12px;
                right: -12px;
                z-index: 9001;
                color: #aaaaaa;
            }
            #trailer-video {
                width: 100%;
                height: 100%;
            }
            .scale-media {
            padding-bottom: 56.25%;
            position: relative;
            }
            .text-center {
            margin-bottom: 20px;
            padding-top: 20px;
             }
            .text-center:hover { 
                background-color: #EEE; cursor: pointer; 
                }
            .scale-media iframe {
                border: none;
                height: 100%;
                position: absolute;
                width: 100%;
                left: 0;
                top: 0;
                background-color: white;
            }
            .modal-content h2{
                text-alignment: center;
            }
            .align {
                display: inline-block;
            }
        </style>
            '''
# Javascript section
main_page_head_2 = '''
        <script type="text/javascript" charset="utf-8">
        {js_snippets}
        </script>
    </head>
'''

# Replicate this snippet for each movie added to data-bind their individual dates and descriptions
javascript_snippet = '''
   
    // Pause the video when the modal is closed
    $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {{
        // Remove the src so the player itself gets removed, as this is the only
        // reliable way to ensure the video stops playing in IE
        $("#trailer-video-container-{movie_id}").empty();
    }});
    // Start playing the video whenever the trailer modal is opened
    $(document).on('click', '.movie-tile-{movie_id}', function (event) {{
        var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
        var sourceUrl = 'https://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
        $("#trailer-video-container-{movie_id}").empty().append($("<iframe></iframe>", {{
        'id': 'trailer-video',
        'type': 'text-html',
        'src': sourceUrl,
        'frameborder': 0
        }}));
    }});
'''

# The main page layout and title bar
main_page_content = '''
  <body>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Classic Tomatoes</a>
          </div>
          <p class="navbar-text navbar-right">Built by <a href="https://github.com/Banhawy" target="_blank">Adham El Banhawy</a></p>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# a single movie card info html template
movie_card_content = '''
    <!-- Movie Info Modal -->
    <div class="modal" id="poster-{movie_id}">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="container-fluid">
                    <h1>{movie_title}</h1>
                    <h4 class="align">Release Date: </h4>
                    <p class="align">{movie_release_date}</p>
                    <h4>Storyline:</h4>
                    <p>{movie_storyline}</p>
                </div>
                <!--Video Appended Here -->
                <div class="scale-media" id="trailer-video-container-{movie_id}">
                </div>
            </div>
        </div>
    </div>  
    '''

# A single movie entry html template
movie_tile_content = '''
    <div class="col-md-6 col-lg-4 movie-tile movie-tile-{movie_id} no-modal text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#poster-{movie_id}">
        <img src="{poster_image_url}" width="220" height="342">
        <h2>{movie_title}</h2>
        <p><em>{movie_tagline}</em></p>
    </div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            movie_tagline=movie.tagline,
            trailer_youtube_id=movie.youtube_key,
            movie_id=movie.movie_id
        )
        content += movie_card_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            movie_storyline=movie.get_storyline(),
            movie_release_date=movie.release_date,
            movie_id=movie.movie_id
        )
    return content

# This function binds movie_ids to {{movie_id}} targets in javascript section
def create_js_content(movies):
    content = ''
    for movie in movies:
        content += javascript_snippet.format(
            movie_id=movie.movie_id
        )
    return content

def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('classic_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    js_header = main_page_head_2.format(
        js_snippets=create_js_content(movies)
    )


    # Output the file
    output_file.write(main_page_head_1 + js_header + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
