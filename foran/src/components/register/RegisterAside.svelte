<script lang="typescript">
    export let src: string;
    export let alt: string;
    export let header: string;
    export let width: string = "36%";
</script>

<aside class="image" style="width:{width};">
    <p>{header}</p>
    <img {src} {alt}>
</aside>


<style>
    .image{
        display: flex;
        padding-top: 1rem;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        height: 100%;
        background-color: var(--color-3);
    }

    .image p{
        color: white;
        font-family: "Roboto Condensed";
        font-size: 1.4em; 
    }

    .image img{
        margin-top: 3em;
        max-width: 90%;
        max-height: 90%;
    }
</style>
