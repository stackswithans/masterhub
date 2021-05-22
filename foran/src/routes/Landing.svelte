<script lang="typescript">
    import ButtonLink from "../components/ButtonLink.svelte";
    import Brand from "../components/Brand.svelte";
    import NavBar from "../components/NavBar.svelte";
</script>


<div class="row">
    <NavBar theme="dark"/>
    <section class="split">
        <div class="brand-text">
            <Brand theme="light" size="3rem"/>
            <p>Aprender nunca foi tão fácil, assasadaddajdkadjakdjajdakjdakj
                Com mestres cheios de vontade e skde conhecimento, 
                Torna-te numa máquina ideal.
            </p>
            <div class="link-button">
                <ButtonLink url="#" width="8.25rem" height="2.25rem" text="Saiba mais" color="--color-7"/>
            </div>
        </div>
        <img src="/assets/images/landing-img-1.png" alt="">
    </section>
</div>
<div class="row">

</div>



<style>
    :global(body){
        background-color: var(--color-8);
    }

    .row{
        width: 100%;
        min-height: 100vh;
    }

    section{
        height:100%;
        font-size: 1rem;
        margin-top: 2rem;
    }

    .brand-text{
        margin-top: 5rem;
        max-width: 25%; 
        max-height: 25%; 
    }

    .brand-text p{
        margin-top: 1rem;
        overflow-wrap: break-word;
    }

    .brand-text .link-button{
        margin-top: 3rem;
    }


    .split{
        display: flex;
        justify-content: space-evenly;
        align-items: flex-start;
        gap: 1rem;
    }

    img{
        max-width: 35%;
        max-height: 35%;
    }
</style>
