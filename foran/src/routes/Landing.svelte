<script lang="typescript">
    import ButtonLink from "../components/ButtonLink.svelte";
    import Brand from "../components/Brand.svelte";
    import NavBar from "../components/NavBar.svelte";
    import LandingInput from "../components/landing/LandingInput.svelte";
    import ContactFormHeader from "../components/landing/ContactFormHeader.svelte";
    import CardGrid from "../components/landing/CardGrid.svelte";
</script>


<section class="row">
    <NavBar theme="dark"/>
    <div class="split">
        <div class="brand-text">
            <Brand theme="dark" size="3rem"/>
            <p>Aprender nunca foi tão fácil, assasadaddajdkadjakdjajdakjdakj
                Com mestres cheios de vontade e skde conhecimento, 
                Torna-te numa máquina ideal.
            </p>
            <div class="link-button">
                <ButtonLink url="#" width="8.25rem" height="2.25rem" text="Saiba mais" color="--color-7"/>
            </div>
        </div>
        <img src="/assets/images/landing-img-1.png" alt="A student taking online classes">
    </div>
</section>

<section class="row">
    <header id="section-2-header">
        <h1> <span style="color:var(--color-5);">Porquê</span> escolher o MasterHub?</h1>
        <p>Só aqui é que receberá educação de classe mundial,  O MasterHub oferece a oportunidade de interagir com experts em diversas áreas do conhecimento.</p> 

    </header>
    <div id="section-2-content">
        <img src="/assets/images/landing-img-2.png" alt="Person explaining statistics">
        <CardGrid/>
    </div>
</section>

<section class="row">
    <div>
        <ContactFormHeader/>
        <LandingInput label="Nome completo"/>
        <LandingInput label="Email"/>
        <LandingInput label="Assunto"/>
        <LandingInput large={true} label="Escreva a sua mensagem aqui"/>
    </div>
    <img src="/assets/images/landing-contact.png" alt="Woman talking on the phone">
</section>

<style>
    :global(body){
        background-color: var(--color-8);
    }

    .row{
        width: 100%;
        min-height: 100vh
    }

    .brand-text{
        margin-top: 5rem;
        max-width: 25%; 
        max-height: 25%; 
    }

    .brand-text p{
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

    .row:first-child  img{
        max-width: 40%;
        max-height: 40%;
    }

    .row:nth-child(2) {
        padding-top: 3rem;
    }

    #section-2-header{
        text-align: center;
        margin-bottom: 2.4rem;
    }

    #section-2-header h1{
        font-size: 2rem;
        margin-bottom: 1rem;
    }

    #section-2-header p{
        max-width: 75%;
        margin: auto;
        overflow-wrap: break-word;
    }

    #section-2-content{
        display: flex;
        justify-content: space-evenly;
    }

    #section-2-content img{
        max-width: 35%;
        max-height: 35%;
    }

    .row:nth-child(3){
        padding-top: 2rem;
        display: flex;
        justify-content: space-evenly;
        align-items: flex-start;
    }

    .row:nth-child(3) img{
        max-width: 45%;
        max-height: 45%;
    }

    @media(max-width: 1366px){
        .split{
            margin-top: 1rem;
        }
    }

    @media(max-width: 1200px){
        .split{
            margin-top: 2rem;
        }

        :global(html){
            font-size: 12px;
        }
    }

    @media(max-width: 1024px){
        .split{
            margin-top: 3rem;
        }

        :global(html){
            font-size: 12px;
        }
    }
</style>
