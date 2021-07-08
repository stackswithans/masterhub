<script lang="typescript">
    import { isLoggedIn, logOut} from "../scripts/auth";
    import { push } from "svelte-spa-router";
    import ButtonLink from "../components/ButtonLink.svelte";

    let name; 

    if(!isLoggedIn()){
        push("/login");
        console.log("hello")
    }
    else{
        if(window.localStorage.getItem("utype") === "ST" || window.localStorage.getItem("activated") === "true"){
            push("/search");
        }
        else{
            name = window.localStorage.getItem("name");
            logOut();
        }
    }

</script>



<main class="container">
    <p>
        
        Olá mestre {name}, parece que a sua conta ainda não foi activada (Entraremos em contacto consigo). 
        Porquê que não aprende com outros mestres enquanto aguarda pela sua entrevista!?
    </p>
    <ButtonLink url="#/search" width="8.25rem" height="2.25rem" text="Explorar" color="--7"/>
</main>


<style>
    .container{
        width: 100vw;
        height: 100vh; 
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        background-color: var(--color-8);
    }

    p{
        color: black;
        margin: 1rem 0;
        width: 50ch;
    }
</style>



