<script lang="typescript">
    import { link } from "svelte-routing";

    export let url: string;
    export let text: string;
    export let color: string;
    export let width: string;
    export let height: string;
    let styles = `
        color: var(${color});
        width: ${width};
        height: ${height};
    `;
</script>
    

<a href="{url}" use:link style="{styles}">{text}</a>


<style>
    a {
        display: flex;
        justify-content: center;
        align-items: center;
        text-decoration: none;
        font-size: 1rem;
        background-color: var(--color-2);
        border-radius: 2rem;
        font-weight: bold;
    }

    a:hover{
        cursor: pointer;
    }
</style>
