<script lang="typescript">
    import NavLink from "./NavLink.svelte";
    export let theme: string;

    let color = (theme === "dark")? "--color-3": "--color-7";
</script>


<header>
    <ul>
        <NavLink text="Acerca" {color}/>
        <NavLink text="Quero Aprender" {color}/>
        <NavLink text="Quero Ensinar" {color}/>
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
    }
</style>
