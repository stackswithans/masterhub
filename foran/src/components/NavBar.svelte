<script lang="typescript">
    import NavLink from "./NavLink.svelte";
</script>


<header>
    <ul>
        <NavLink text="Acerca" color="--color-3"/>
        <NavLink text="Quero Aprender" color="--color-3"/>
        <NavLink text="Quero Ensinar" color="--color-3"/>
    </ul>
</header>



<style>
    header{
        display: flex;
        align-items: flex-end;
        width: 100%;
        min-height: 5.0625rem;
        padding: 0 3rem 0 0;
    }

    header ul{
        display: flex;
        flex-grow: 1;
        justify-content: flex-end;
        gap: 1rem;
        font-family:"Roboto", sans-serif; 
    }
</style>
