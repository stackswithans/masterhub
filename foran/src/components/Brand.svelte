
<script lang="typescript">
    export let theme: string;
    export let size: string;

    let hColor = (theme === "dark")? "--color-2" : "--color-7"; 
</script>


<h1 style="font-size:{size}"><span style="color:var({hColor});">Master</span>Hub</h1>


<style>
    h1, 
    span{
        font-family:"Roboto Slab";
    }
</style>
