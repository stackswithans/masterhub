<script lang="typescript">
    import { isLoggedIn, logOut }  from "../scripts/auth";
    import NavLink from "./NavLink.svelte";
    import ButtonLink from "./ButtonLink.svelte";
    import Brand from "./Brand.svelte"

    export let theme: string;
    export let brand: boolean;
    let color = (theme === "dark")? "--color-3": "--color-7";
    let loggedIn = isLoggedIn(); 

    let runLogout = () => {
        logOut();
        loggedIn = isLoggedIn();
    };
</script>


<nav>
    {#if brand}
        <Brand size="2rem" {theme}/>
    {:else}
        <div></div>
    {/if}

    <ul>
        <NavLink url="about" text="Acerca" {color}/>
        {#if loggedIn}
            <NavLink url="home/" text="Central de aulas" {color}/>
            <NavLink on:click={runLogout} url="" text="Terminar sessão" {color}/>
        {:else}
            <NavLink url="register/student" text="Quero Aprender" {color}/>
            <NavLink url="register/master" text="Quero Ensinar" {color}/>
            <ButtonLink url="/login" text="Login" width="7.25rem" height="2.0625rem" color="--color-3"/>
        {/if}
    </ul>
</nav>


<style>
    nav{
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        min-height: 5.0625rem;
        padding: 0 3rem 0 3rem;
    }

    nav p{
        font-family: Roboto;
        color: white;
    }

    nav ul{
        display: flex;
        flex-grow: 1;
        justify-content: flex-end;
        align-items: center;
        gap: 1rem;
    }
</style>
