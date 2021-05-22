<script lang="typescript">
    import NavLink from "./NavLink.svelte";
    import ButtonLink from "./ButtonLink.svelte";
    import Brand from "./Brand.svelte"
    export let theme: string;

    let color = (theme === "dark")? "--color-3": "--color-7";
</script>


<header>
    <ul>
        <NavLink url="#" text="Acerca" {color}/>
        <NavLink url="#" text="Quero Aprender" {color}/>
        <NavLink url="#" text="Quero Ensinar" {color}/>
        <ButtonLink url="#" text="Login" width="7.25rem" height="2.0625rem" color="--color-3"/>
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
        align-items: center;
        gap: 1rem;
    }
</style>
