<script>
    export let description = "";
</script>

<div class="main">
    <button class="button">{description}</button>
</div>

<style>
    .main{
        padding: 1rem;
    }

    .button{
        font-family: "Roboto";
        font-size: 1.2rem;
        color: white;
        background-color: var(--color-1);
        border: 0px solid black;
        width: 20rem;
        border-radius: 25px;
    }

</style>