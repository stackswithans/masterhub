<script>
    export let description = "";
</script>

<div>
    <input type="text" placeholder={description} class="input-after">
</div>

<style>
    div{
        padding: 1rem;
        width: 20rem;
    }

    .input-after{
        width: 18rem;
        border-radius: 5px;
        text-indent: 1rem;
    }

    .input-after::placeholder{
        color: var(--color-6);
        font-size: 1.2rem;
        font-family: "Roboto Condensed";
    }

    .input-after:focus{
        outline: none;
    }

</style>