<script>
    export let description = "";
</script>

<div class="main">
    <label class="description">{description}</label>
    <div class="loader"></div>
</div>

<style>
    .main{
        padding: 1rem;
        width: 30rem;
    }

    .description{
        position: relative;
        width: 100%;
        font-family: "Roboto";
        font-weight: bold;
        font-size: 1.8rem;
        color: var(--color-3);
    }

    .loader{
        width: 6rem;
        height: 0.7rem;
        border-radius: 5px;
        background-color: var(--color-1);
        margin-top: 0.5rem;
    }

</style>