<script lang="typescript">


</script>
    <main>
        <aside class="side-bar">
            <div>
                <h1>Master<span>Hub</span></h1>
            </div>
            <div class="menu-list">
                <ul>
                    <li><a href=""><i class="fas fa-home"></i>Home</a></li>
                    <li><a href=""><i class="far fa-calendar-alt"></i>Horário</a></li>
                    <li><a href=""><i class="fas fa-video"></i>Sala</a></li>
                </ul>
            </div>
            <div class="adds">

            </div>
        </aside>
        <div class="container">
            <nav class="nav-bar">
                <div class="search-bar">
                    <input type="text" class="bar" placeholder="Pesquise pela habilidade que deseja">
                    <i class="fas fa-search fa-lg"></i>
                </div>
                <div class="profile">
                    <i class="fas fa-bell fa-2x"></i>
                    <div class="sub-profile">
                        <img src="" alt="">
                        <span>Peter P.</span>
                        <i class="fas fa-chevron-down"></i>
                    </div>
                </div>
            </nav>
            <div class="main-container">
                <slot></slot>
            </div>
        </div>
    </main>


<style>
    *{
        padding: 0;
        margin: 0;
    }

    main{
        background-color: var(--color-3);
        display: flex;
    }

    .side-bar{
        width: 15vw;
        height: 100vh;
        background-color: white;
    }

    h1{
        font-family: 'Roboto Slab';
        color: var(--color-1);
        text-align: center;
        font-size: 2rem;
        padding: 1rem 0rem;
    }

    span{
        font-family: 'Roboto Slab';
        color: var(--color-3);
    }

    .menu-list ul{
        padding: 4rem 0rem;
        display: flex;
        flex-direction: column;
    }

    .menu-list ul li{
        padding: 1rem;
        list-style-type: none;
        font-size: 'Amiri';
    }

    .menu-list ul a{
        font-size: 1.2rem;
        text-decoration: none;
        color: var(--color-3);
        font-family: 'Roboto Slab';
        padding: 0.6rem 3rem;
    }

    i{
        padding-right: 1.8rem;
     }

     .menu-list ul a:hover{
         background-color: var(--color-1);
         border-radius: 5px;
         font-weight: bolder;
     }

     .adds{
         width: 10vw;
         height: 16vh;
         border: 1px solid var(--color-3);
         margin: auto;
         border-radius: 5px;
         margin-top: 20rem;
     }

     .nav-bar{
        background-color: var(--color-4);
        width: 85vw;
        height: 100%;
        display: flex;
        padding: 1rem;
     }

     .search-bar{
         background-color: var(--color-4);
         border-radius: 25px;
         border: 1px solid grey;
         width: 30rem;
         height: 3rem;
     }

     .search-bar input{
         width: 86%;
         height: 100%;
         border-radius: 30px;
         border: 0px solid black;
         text-indent: 1rem;
     }

     .fa-search{
         color: white;
         border-radius: 30px;
         background-color:var(--color-3);
         padding: 0.6rem;
     }

     .search-bar input:focus{
         outline: none;
     }

     .search-bar input::placeholder{
         opacity: 0.5;
     }

     .profile{
         width: 10rem;
         display: flex;
         padding: 0.4rem;
         margin-left: 40rem;
     }

     .sub-profile{
         display: flex;
         border-left: 2px solid grey;
         padding: 0.5rem;
     }

     .sub-profile span{
         width: 5vw;
         padding: 0.3rem;
     }

     .sub-profile img{
         width: 2rem;
         height: 2rem;
         border: 1px solid grey;
         border-radius: 20px;
     }

     .fa-bell{
        margin: auto;
     }

     .fa-chevron-down{
        padding: 0.4rem;
     }

     .main-container{
         background-color: rgb(224, 224, 224);
         width: 85vw;
         height: 90vh;
     }

</style>