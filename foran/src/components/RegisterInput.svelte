<script>
    export let description = "";
</script>

<div>
    <label class="description">{description}</label>
    <input type="text" class="input-after">
</div>

<style>
    div{
        padding: 1rem;
        width: 17rem;
    }

    .description{
        position: relative;
        width: 100%;
        font-family: "Roboto";
        font-weight: bold;
        font-size: 1.2rem;
        color: var(--color-3);
    }

    .input-after{
        width: 15rem;
        margin-top: 1rem;
        border-radius: 5px;
    }

    .input-after:focus{
        outline: none;
    }

</style>