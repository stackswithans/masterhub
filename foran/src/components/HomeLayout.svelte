<script lang="typescript">
    import Brand from "./Brand.svelte";

</script>
    <main>
        <aside class="side-bar">
            <div class="logo">
                <Brand theme="dark" size=100%/>
            </div>
                <ul class="menu-list">
                    <li><a href=""><i class="fas fa-home"></i>Home</a></li>
                    <li><a href=""><i class="far fa-calendar-alt"></i>Horário</a></li>
                    <li><a href=""><i class="fas fa-video"></i>Sala</a></li>
                </ul>
        </aside>
        <div class="container">
            <nav class="nav-bar">
                <div class="search-bar">
                    <input type="text" class="bar" placeholder="Pesquise pela habilidade que deseja">
                    <i class="fas fa-search fa-sm"></i>
                </div>
                <div class="profile">
                    <i class="fas fa-bell fa-lg"></i>
                    <div class="sub-profile">
                        <img src="" alt="">
                        <span>Migue Voa</span>
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

    main{
        width: 100%;
        height: 100vh;
        display: flex;
    }


    .side-bar{
        background-color: white;
        display: flex;
        flex-direction: column;
        height: 100%;
        padding: 1rem 0;
        gap: 4rem;
        width: 12%;
        align-items: center;
    }

    .menu-list{
        display: flex;
        flex-direction: column;
        gap: 1.6em;
    }

    .menu-list li{
        display: flex;
        list-style-type: none;
    }

    .menu-list a{
        display: flex;
        align-items: center;
        gap: 1em;
        color: var(--color-3);
        padding: 0.2em 0.8em;
    }

     .menu-list li:hover{
         background-color: var(--color-1);
         border-radius: 1rem;
         font-weight: bolder;
         text-decoration: none;
     }

     .menu-list a:hover{
         text-decoration: none;
     }

     .container{
         width: 88%;
         background-color: var(--color-8);
         height: 100%;
     }

     .nav-bar{
         width: 100%;
         background-color: white;
         height: 7%;
         display: flex;
         justify-content: space-between;
         align-items: center;
         padding: 0 2rem;
     }

     .search-bar{
         background-color: white;
         border-radius: 25px;
         border: 2px solid grey;
         width: 30%;
         max-height: 70%;
         display: flex;
         align-items: center;
         padding: 0.2rem;
         justify-content: space-between;
         padding: 0.1em 0.2em;
     }

     .bar{
         display: flex;
         width: 90%;
         margin: 0;
         border-radius: 50px;
         border: 0px solid black;
         padding: 0;
     }

     .fa-search{
         background-color: var(--color-3);
         border-radius: 40px;
         color: white;
         padding: 0.2em;
     }

     .search-bar input:focus{
         outline: none;
     }

     .search-bar input::placeholder{
         opacity: 0.5;
         font-size: 0.75em;
         font-family: 'Roboto';
     }

     .profile{
         display: flex;
         align-items: center;
     }

     .sub-profile{
         display: flex;
         align-items: center;
         gap: 0.5rem;
     }

     .sub-profile span{
        font-family: 'Roboto Slab';
        font-size: 0.8em;
     }

     .sub-profile img{
         width: 2rem;
         height: 2rem;
         border: 1px solid grey;
         border-radius: 20px;
     }

     .fa-bell{
         margin: 0 0.4em;
         padding: 0 0.4em;
         border-right: 1px solid black;
     }

</style>