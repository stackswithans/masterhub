
<script lang="typescript">
    import { push } from "svelte-spa-router";
    export let theme: string;
    export let size: string;

    let hColor = (theme === "dark")? "--color-2" : "--color-7"; 
</script>


<h1 on:click="{() =>{ push('/');}}" style="font-size:{size}"><span style="color:var({hColor});">Master</span>Hub</h1>


<style>
    h1, 
    span{
        font-family:"Roboto Slab";
    }

    h1:hover{
        cursor: pointer;
    }
</style>
