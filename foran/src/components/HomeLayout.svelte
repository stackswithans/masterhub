<script lang="typescript">
    import Brand from "./Brand.svelte";

</script>
    <main>
        <aside class="side-bar">
            <div>
                <Brand theme="dark"/>
            </div>
                <ul class="menu-list">
                    <li><a href=""><i class="fas fa-home"></i>Home</a></li>
                    <li><a href=""><i class="far fa-calendar-alt"></i>Horário</a></li>
                    <li><a href=""><i class="fas fa-video"></i>Sala</a></li>
                </ul>
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
                    <div class="separador"></div>
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
        width: 100%;
        gap: 1rem;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .menu-list li{
        display: flex;
        list-style-type: none;
        width: 100%;
        padding: 1rem 2rem;
    }

    .menu-list a{
        align-items: center;
        display: flex;
        font-size: 1.2rem;
        text-decoration: none;
        color: var(--color-3);
        font-family: 'Roboto Slab';
    }

    i{
        padding-right: 1rem;
     }

     .menu-list li:hover{
         background-color: var(--color-1);
         border-radius: 1rem;
         font-weight: bolder;
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
     }

     .search-bar input{
         width: 90%;
         height: 100%;
         border-radius: 40px;
         border: 0px solid black;
         text-indent: 1rem;
         background-color: white;
         margin: auto 0;
     }

     .fa-search{
         color: white;
         border-radius: 40px;
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
     }

     .sub-profile img{
         width: 2rem;
         height: 2rem;
         border: 1px solid grey;
         border-radius: 20px;
     }

     .separador{
         width: 1px;
         background-color: var(--color-3);
         height: 1.8rem;
        margin-right: 1rem;
     }

</style>