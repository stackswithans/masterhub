<script lang="typescript">
    export let icon: string;
    export let title: string;
    export let text: string;
    export let bgColor: string;
    export let bColor: string;

    const inlineStyles = `
        --border-color: var(${bColor});
        background-color: var(${bgColor});
    `
</script>


<div style="{inlineStyles}">
    <img src="{icon}" alt="">
    <h1>{title}</h1>
    <p>{text}</p>
</div>

<style>
    div{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        padding: 2rem 0.2rem 2rem 0.2rem;
        text-align: center;
        gap: 1.5rem;
        border: 2px solid var(--border-color);
        border-radius: 1rem;
        box-shadow: 0px 0px 1rem -10px black;
    }

    div h1{
        font-family: "Roboto slab";
        font-size: 1.1rem;
    }

    div img{
        max-width: 20%;
        max-height: 20%;
    }
</style>
