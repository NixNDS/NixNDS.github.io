<!DOCTYPE html>
<!--
  Daraz by TEMPLATE STOCK
  templatestock.co @templatestock
  Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
-->

<html lang="en">

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>St Laurent - Spécialité NSI</title>

  <link rel="stylesheet" href="css/bootstrap.min.css" />
  <link rel="stylesheet" href="css/fontawesome.min.css" />
  <link rel="stylesheet" href="css/animate.css" />

  <link rel="stylesheet" href="css/style.css" />
  <link rel="stylesheet" href="css/eleve.css" />

  <script type="text/javascript" src="js/jquery-1.11.2.min.js"></script>
  <script type="text/javascript" src="js/bootstrap.min.js"></script>
  <script type="text/javascript"
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCZXJBVDf7R4JqmSpopVPoduIGWx1IwpBM"></script>
  <script type="text/javascript" src="js/plugins.js"></script>
  <!-- Font Awesome v5 -->
  <script src="https://kit.fontawesome.com/bef258002f.js" crossorigin="anonymous"></script>

  <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
  <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body>
  <div class="svg-wrap">
    <svg width="64" height="64" viewBox="0 0 64 64">
      <path id="arrow-left"
        d="M26.667 10.667q1.104 0 1.885 0.781t0.781 1.885q0 1.125-0.792 1.896l-14.104 14.104h41.563q1.104 0 1.885 0.781t0.781 1.885-0.781 1.885-1.885 0.781h-41.563l14.104 14.104q0.792 0.771 0.792 1.896 0 1.104-0.781 1.885t-1.885 0.781q-1.125 0-1.896-0.771l-18.667-18.667q-0.771-0.813-0.771-1.896t0.771-1.896l18.667-18.667q0.792-0.771 1.896-0.771z">
      </path>
    </svg>

    <svg width="64" height="64" viewBox="0 0 64 64">
      <path id="arrow-right"
        d="M37.333 10.667q1.125 0 1.896 0.771l18.667 18.667q0.771 0.771 0.771 1.896t-0.771 1.896l-18.667 18.667q-0.771 0.771-1.896 0.771-1.146 0-1.906-0.76t-0.76-1.906q0-1.125 0.771-1.896l14.125-14.104h-41.563q-1.104 0-1.885-0.781t-0.781-1.885 0.781-1.885 1.885-0.781h41.563l-14.125-14.104q-0.771-0.771-0.771-1.896 0-1.146 0.76-1.906t1.906-0.76z">
      </path>
    </svg>
  </div>


  <!-- MAIN CONTENT -->

  <div class="container-fluid">

    <!-- HEADER -->

    <section id="header">

      <!-- NAVIGATION -->
      <nav class="navbar navbar-fixed-top navbar-default bottom">
        <div class="container">
          <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#menu">
              <span class="sr-only">Toggle navigation</span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#header"><img src="Images/StLaurentlaPaix.png" width="20%"></a>
          </div><!-- /.navbar-header -->

          <div class="collapse navbar-collapse" id="menu">
            <ul class="nav navbar-nav navbar-right">
              <li><a href="#header"><i class="fas fa-home fa-2x"></i> Home</a></li>
              <li><a href="#about"><i class="fas fa-info-circle fa-2x"></i> About</a></li>
              <li><a href="#cv"><i class="fas fa-user-ninja fa-2x"></i> Resume</a></li>
              <li><a href="#portfolio"><i class="fas fa-camera fa-2x"></i> Portfolio</a></li>
              <li><a href="#info"><i class="fas fa-dice-d20 fa-2x"></i> Skills</a></li>
              <li><a href="#contact"><i class="fas fa-envelope fa-2x"></i> Contact</a></li>
            </ul>
          </div> <!-- /.navbar-collapse -->
        </div> <!-- /.container -->
      </nav>

      <!-- SLIDER -->
      <div class="header-slide">
        <section>
          <div id="loader" class="pageload-overlay" data-opening="M 0,0 0,60 80,60 80,0 z M 80,0 40,30 0,60 40,30 z">
            <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 80 60"
              preserveAspectRatio="none">
              <path d="M 0,0 0,60 80,60 80,0 Z M 80,0 80,60 0,60 0,0 Z" />
            </svg>
          </div> <!-- /.pageload-overlay -->

          <div class="image-slide bg-fixed">
            <div class="overlay">
              <div class="container">
                <div class="row">
                  <div class="col-md-12">

                    <div class="slider-content">
                      <h1></h1>
                      <p>Site de la Spécialité NSI en 1ère</p>
                    </div>

                  </div> <!-- /.col-md-12 -->
                </div> <!-- /.row -->
              </div> <!-- /.container -->
            </div> <!-- /.overlay -->
          </div> <!-- /.image-slide -->

          <nav class="nav-slide">
            <a class="prev" href="#prev">
              <span class="icon-wrap">
                <svg class="icon" width="32" height="32" viewBox="0 0 64 64">
                  <use xlink:href="#arrow-left">
                </svg>
              </span>
              <div>
                <span>Prev Photo</span>
                <h3>...</h3>
                <p>...</p>
                <img alt="Previous thumb">
              </div>
            </a>
            <a class="next" href="#next">
              <span class="icon-wrap">
                <svg class="icon" width="32" height="32" viewBox="0 0 64 64">
                  <use xlink:href="#arrow-right">
                </svg>
              </span>
              <div>
                <span>Next Photo</span>
                <h3>...</h3>
                <p>...</p>
                <img alt="Next thumb">
              </div>
            </a>
          </nav>
        </section>

        <script type="text/javascript">
          var dataHeader = [
            {
              bigImage: "Images/slide-1.jpg",
              title: "Spécialité NSI",
              author: "Templatestock"
            },
            {
              bigImage: "Images/slide-2.jpg",
              title: "Portfolio",
              author: "Templatestock"
            },
            {
              bigImage: "Images/slide-team-unsplash.jpg",
              title: "Team Spirit",
              author: "Unsplash"
            }
          ],
            loaderSVG = new SVGLoader(document.getElementById('loader'), { speedIn: 600, speedOut: 600, easingIn: mina.easeinout });
          loaderSVG.show()

          // Update the slider content with the correct information
          function updateSliderContent(index) {
            var slide = dataHeader[index];
            document.querySelector(".slider-content h1").innerHTML = slide.title;
            document.querySelector(".nav-slide .prev h3").innerHTML = dataHeader[index === 0 ? dataHeader.length - 1 : index - 1].title;
            document.querySelector(".nav-slide .next h3").innerHTML = dataHeader[index === dataHeader.length - 1 ? 0 : index + 1].title;
          }
          
          // Initial update of the slider content
          updateSliderContent(0);
          
          // Add event listeners for previous and next slide navigation
          document.querySelector(".nav-slide .prev").addEventListener("click", function() {
            var index = dataHeader.findIndex(slide => slide.title === document.querySelector(".slider-content h1").innerHTML);
            updateSliderContent(index === 0 ? dataHeader.length - 1 : index - 1);
          });
          
          document.querySelector(".nav-slide .next").addEventListener("click", function() {
            var index = dataHeader.findIndex(slide => slide.title === document.querySelector(".slider-content h1").innerHTML);
            updateSliderContent(index === dataHeader.length - 1 ? 0 : index + 1);
          });

          /* When the user clicks on the button, toggle between hiding and showing the dropdown content */
          function clicDrop() {
            document.getElementById("myDropdown").classList.toggle("show");
          }

          // Close the dropdown if the user clicks outside of it
          window.onclick = function (e) {
            if (!e.target.matches('.dropbtn')) {
              var myDropdown = document.getElementById("myDropdown");
              if (myDropdown.classList.contains('show')) {
                myDropdown.classList.remove('show');
              }
            }
          }

        </script>

      </div><!-- /.header-slide -->
    </section>

    <!-- HEADER END -->


    <!-- ABOUT -->

    <section id="about" class="light">
      <header class="title">
        <h2>Rafael <span>NOGUEIRA DA SILVA</span></h2>
        <p>Présentation de l'élève et de ses <strong>projets</strong> cette année en <strong>NSI</strong></p>
      </header>

      <div class="container">
        <div class="row table-row">
          <div class="col-sm-6 hidden-xs">
            <div class="section-content">
              <div class="big-image" style="background-image:url(Images/Steve.png)"></div>
            </div>
          </div>

          <div class="col-sm-6">
            <div class="section-content">
              <div class="about-content left animated" data-animate="fadeInLeft">
                <div class="about-icon"><i class="fab fa-html5"></i></div>
                <div class="about-detail">
                  <h4>Projets Web</h4>
                  <p>Création d'un site internet avec utilisation de javascript (légèrement) et de css.</p>
                </div>
              </div>

              <div class="about-content left animated" data-animate="fadeInLeft">
                <div class="about-icon"><i class="fab fa-python"></i></div>
                <div class="about-detail">
                  <h4>Projets Python</h4>
                  <p>Création d'un jeu de pendu. J'ai réalisé un travail sur les arbres binaires pour but d'aider à la décision pour l'assistance aux premiers secours.</p>
                </div>
              </div>

              <div class="about-content left animated" data-animate="fadeInLeft">
                <div class="about-icon"><i class="fa fa-code"></i></div>
                <div class="about-detail">
                  <h4>Autres</h4>
                  <p>J'ai aussi réalisé des projets en SQL, afin de gérer la base de données d'un jeu de plateau.J'ai participer au concours Algoréa.</p>
                </div>
              </div>
            </div>
          </div>
        </div> <!-- /.row table-row -->
      </div> <!-- /.container -->
    </section>

    <!--CV -->
    <section id="cv" class="light">
      <header class="title">
        <h2>Mon <span>CV</span></h2>
        <p>About me (again...)</p>
      </header>
        <div class="container">
            <div class="row">
                <div class="col-md-6 col-lg-4">
                    <div class="card">
                       <div class="card-header">
                            <div class="mt-2">
                                <h4>Expérience Professionnelle</h4>
                                <span class="line"></span>  
                            </div>
                        </div>
                        <div class="card-body">
                            <h6 class="title text-danger"> ÉTÉ 2023</h6>
                            <P>Animateur</P>
                            <P class="subtitle">Détenteur du BAFA, j'ai travaillé dans un accueil de jeunesse, avec une tranche d'âge de 6 à 11 ans.</P>
                            <hr>
                            <h6 class="title text-danger">2022-2023</h6>
                            <P>Petit travail</P>
                            <P class="subtitle">J'ai pu travailler, aidant mes voisins, dans les tâches du jardinage. </P>
                            <hr>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4">
                    <div class="card">
                       <div class="card-header">
                            <div class="mt-2">
                                <h4>Expérience Personnelle</h4>
                                <span class="line"></span>  
                            </div>
                        </div>
                        <div class="card-body">
                            <h6 class="title text-danger">2017 - Present</h6>
                            <P>Permis de conduire</P>
                            <P class="subtitle">Détenteur du code, je suis en conduite accompagnée, et je vais bientôt passer l'examen du permis.</P>
                            
                        </div>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="card">
                       <div class="card-header">
                            <div class="pull-left">
                                <h4 class="mt-2">Compétences</h4>
                                <span class="line"></span>  
                            </div>
                        </div>
                        <div class="card-body pb-2">
                           <h6>HTML &amp; CSS</h6>
                            <div class="progress mb-3">
                                <div class="progress-bar bg-danger" role="progressbar" style="width: 30%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                            <h6>JavaScript</h6>
                            <div class="progress mb-3">
                                <div class="progress-bar bg-danger" role="progressbar" style="width: 10%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                            <h6>Python</h6>
                            <div class="progress mb-3">
                                <div class="progress-bar bg-danger" role="progressbar" style="width: 70%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                            <h6>SQL</h6>
                            <div class="progress mb-3">
                                <div class="progress-bar bg-danger" role="progressbar" style="width: 60%" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                            
                        </div>
                    </div>
                    <div class="card">
                       <div class="card-header">
                            <div class="pull-left">
                                <h4 class="mt-2">Languages</h4>
                                <span class="line"></span>  
                            </div>
                        </div>
                        <div class="card-body pb-2">
							<h6>Português</h6>
                            <div class="progress mb-3">
                                <div class="progress-bar bg-danger" role="progressbar" style="width: 100%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
							</div>
							<h6>English</h6>
                            <div class="progress mb-3">
                                <div class="progress-bar bg-danger" role="progressbar" style="width: 85%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                             <h6>Français</h6>
                            <div class="progress mb-3">
                                <div class="progress-bar bg-danger" role="progressbar" style="width: 100%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                            <h6>Spanish</h6>
                            <div class="progress mb-3">
                                <div class="progress-bar bg-danger" role="progressbar" style="width: 70%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- PORTFOLIO -->

    <section id="portfolio" class="light">
      <header class="title">
        <h2>Portfolio</h2>
        <p>Mes superbes <strong>projets</strong> !</p>
      </header>

      <div class="container-fluid">
        <div class="row">
          <ul id="filters" class="list-inline">
            <li data-filter="all" class="filter">All</li>
            <li data-filter=".python" class="filter"><i class="fab fa-python"></i> Python</li>
            <li data-filter=".cool-websites" class="filter"><i class="fab fa-html5"></i> HTML</li>
            <li data-filter=".video" class="filter"><i class="fas fa-video"></i> Video</li>
          </ul>
        </div>

        <div class="row">
          <div class="container-portfolio">
            <!-- PORTFOLIO OBJECT -->
            <script type="text/javascript">
              var portfolio = [
                {
                  category: "cool-websites",
                  image: "Images/espace.png",
                  title: "<span>Espace</span> Info",
                  link: "./mini_site_vide/index.html",
                  text: "Un site sur l'espace"
                },
                {
                  category: "video",
                  image: "Images/the_egg.png",
                  title: "Magnifique <span>vidéo</span>",
                  link: "https://youtu.be/h6fcK_fRYaI?feature=shared",
                  text: "Ma video préférée que je vous conseille fortement."
                },
                {
                  category: "python",
                  image: "Images/pendu.png",
                  title: "The <span>Pendu</span>",
                  link: "./code/pendu.py",
                  text: "Le meilleur jeu du pendu de tous les temps",
				  
                },
				{
                  category: "python",
                  image: "Images/Pokemon.png",
                  title: "<span>Pokémon</span>",
                  link: "./code/Class_.py",
                  text: "Le meilleur simulateur de combats Pokémon (by me)",
				  
                },
              ];
            </script>
          </div>
        </div>
      </div>
    </section>

    <!-- INFO -->

    <section id="info" class="dark">
      <header class="title">
        <h2>Compétences</h2>
        <p>Les compétences que j'ai développées ici !</p>
      </header>

      <div class="container experties">
        <div class="row">
          <div class="col-md-6">
            <div class="skill">
              <ul class="skill-bar list-unstyled">
                <li><span class="percentage" data-value="100%"></span><em>Autonomie & initiative</em></li>
                <li><span class="percentage" data-value="90%"></span><em>Créativité</em></li>
                <li><span class="percentage" data-value="100%"></span><em>Coopération</em></li>
                <li><span class="percentage" data-value="100%"></span><em>Apprentissage par l'erreur</em></li>
              </ul>
            </div>
          </div>

          <div class="col-md-6">
            <div class="skill">
              <ul class="skill-bar list-unstyled">
                <li><span class="percentage" data-value="70%"></span><em>Développement Python</em></li>
                <li><span class="percentage" data-value="50%"></span><em>Développement HTML CSS</em></li>
                <li><span class="percentage" data-value="60%"></span><em>Développement de documents</em></li>
                <li><span class="percentage" data-value="70%"></span><em>Informatique théorique</em></li>
              </ul>
            </div>
          </div>
        </div>
      </div> <!-- /.container -->
    </section>


    <section class="separator blue">
      <div class="container">
        <div class="row">
          <div class="col-md-3 col-sm-6 col-xs-6">
            <div class="counter animated" data-animate="fadeInUp" data-delay="0">
              <div class="counter-icon">
                <i class="fa fa-group"></i>
              </div>
              <div class="counter-content">
                
              </div>
            </div>
          </div>

          <div class="col-md-3 col-sm-6 col-xs-6">
            <div class="counter animated" data-animate="fadeInUp" data-delay="500">
              <div class="counter-icon">
                <i class="fa fa-leaf"></i>
              </div>
              <div class="counter-content">
                
              </div>
            </div>
          </div>

          <div class="col-md-3 col-sm-6 col-xs-6">
            <div class="counter animated" data-animate="fadeInUp" data-delay="1000">
              <div class="counter-icon">
                <i class="fa fa-gears"></i>
              </div>
              <div class="counter-content">
                
                
              </div>
            </div>
          </div>

          <div class="col-md-3 col-sm-6 col-xs-6">
            <div class="counter animated" data-animate="fadeInUp" data-delay="1500">
              <div class="counter-icon">
                <i class="fa fa-inbox"></i>
              </div>
              <div class="counter-content">
                
                
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>


    <!-- FOOTER CONTACT -->

    <section id="contact" class="dark">
      <header class="title">
        <h2>Me <span>Contacter</span></h2>
        <p>Pour plus d'information, n'hésitez pas à m'envoyer un message !</p>
      </header>

      <div class="container">
        <div class="row">
          <div class="col-md-8 animated" data-animate="fadeInLeft">
            <form action="mailto:rafael.nogueiradasilva06@gmail.com" method="post" enctype="text/plain">
              <div class="row">
                <div class="col-md-6">
                  <input type="text" name="name" class="form-control" placeholder="Votre Nom">
                </div>
                <div class="col-md-6">
                  <input type="email" name="email" class="form-control" placeholder="Votre E-mail">
                </div>
                <div class="col-md-12">
                  <textarea name="message" class="form-control" rows="3" placeholder="Dites-nous tout !"></textarea>
                </div>
                <div class="col-md-12">
                  <button type="submit" class="btn btn-default submit">Envoyer</button>
                </div>
              </div>
            </form>
          </div>

          <div class="col-md-4 animated" data-animate="fadeInRight">
            <address>
              <span><i class="fa fa-map-marker fa-lg"></i> 1bis chemin de l'autostrade <br>77400 Lagny-sur-Marne</span>
            <div class="map">
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d927.8319950844271!2d2.700710497597743!3d48.871458484029205!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47e61b168ac4021d%3A0x90a1cb36c5aa7b1b!2s1%20Chem.%20de%20l&#39;Autostrade%20Ter%2C%2077400%20Lagny-sur-Marne!5e0!3m2!1sfr!2sfr!4v1710239402570!5m2!1sfr!2sfr" width="600" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
              <span><i class="fa fa-phone fa-lg"></i> 06 52 39 56 91</span>
              <span><i class="fa fa-envelope-o fa-lg"></i> <a
                  href="mailto:rafael.nogueiradasilva06@gmail.com">rafael.nogueiradasilva06@gmail.com</a></span>
              <span><i class="fa fa-globe fa-lg"></i> <a
                  href="http://www.maristes-stlaurent77.fr/fr/page/lycee-presentation" target="_blank">http://www.maristes-stlaurent77.fr/fr/page/lycee-presentation</a></span>
            </address>
          </div>

        </div>
      </div>
    </section>

    <section id="footer">
      <div class="container">
        <div class="row">
          <div class="col-md-12 text-center">
            <p>Made With <i class="fa fa-heart"></i> With the help of the Team Spé NSI</p>
            
          </div>
        </div>
      </div>
    </section>

  </div><!-- /.container-fluid -->

  <!-- SCRIPT -->
  <script type="text/javascript" src="js/main.js">
    // Modal Image Gallery
    function onClick(element) {
      document.getElementById("img01").src = element.src;
      document.getElementById("modal01").style.display = "block";
      var captionText = document.getElementById("caption");
      captionText.innerHTML = element.alt;
    }
  </script>
</body>

</html>
