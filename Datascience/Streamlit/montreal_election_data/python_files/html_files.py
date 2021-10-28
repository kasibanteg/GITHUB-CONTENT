
#<div  style="background-color:#f9caa7">
html_login_style = """
 
 <style>
/* Style the video: 100% width and height to cover the entire window */
#myVideo {
  /*position:fixed;
  right: 0;
  bottom: 0;
  min-width: 100%;
  min-height: 100%; */
  
  object-fit: cover;
  width: 100vw;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;

}

/* Add some content at the bottom of the video/page */
.content {
  position: fixed;
  bottom: 0;
  #top:250;
  background: rgba(0, 0, 0, 0.5);
  color: #f1f1f1;
  width: 100%;
  padding: 20px;
}


h1{
    color:rgb(205,92,92);
    
    
}




 </style>
<body>



<!-- The video -->
<video autoplay muted loop id="myVideo">
  <!--<source src="https://player.vimeo.com/external/179528888.sd.mp4?s=2fa1e3a34d79d660ed1c397b99052757ed298531&profile_id=164" type="video/mp4">-->
<source src="https://player.vimeo.com/external/449623933.sd.mp4?s=63f975b332a83ccf843667b9ca9c5990e290ef09&profile_id=164" type="video/mp4">
</video>

<!-- Optional: some overlay text to describe the video -->
<div class="content">
  <h1>Kwik App Analysis</h1>
  <p>Data science app</p>
  <p>&copy;Kasibante Geoffrey
  <a href='http://www.kasibante.com' target='_blank'>Portfolio</a></p>
  <!-- end description -->
&nbsp;
</div>
</body>




<div>&nbsp;</div>
"""

