
<script lang="typescript">
    import { link } from "svelte-routing";
    let element: HTMLElement;
    export let color: string; 
    export let text: string = ""; 
    export let url: string = ""; 
</script>

<a bind:this={element} style="color:var({color}); border-color:var({color});--highlight-color:var({color});" href="{url}">{text}</a>

<style>
    a{
        text-decoration: None;
        padding: 0.5rem ;
        font-size: 1.1rem;
        font-family:"Roboto", sans-serif; 
    }

    a:hover{
        padding: calc(0.5rem - 3px);
        border-bottom: 3px solid var(--highlight-color);
        border-radius: 2px;
    }
</style>
