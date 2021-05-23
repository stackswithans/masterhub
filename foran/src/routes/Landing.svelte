<script lang="typescript">
    import ButtonLink from "../components/ButtonLink.svelte";
    import Brand from "../components/Brand.svelte";
    import NavBar from "../components/NavBar.svelte";
    import LandingCard from "../components/LandingCard.svelte";
    import LandingInput from "../components/LandingInput.svelte";
</script>


<section class="row">
    <NavBar theme="dark"/>
    <div class="split">
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
        <div id="why-us-cards">
            <LandingCard bColor="--color-2" icon="/assets/icons/landing-class.png" title="Professores" text="Melhores mestres do mundo"/>
            <LandingCard bColor="--color-6" icon="/assets/icons/landing-idea.png" title="Estratégia" text="Melhores mestres do mundo"/>
            <LandingCard bColor="--color-6" icon="/assets/icons/landing-cog.png" title="Fácil" text="Melhores mestres do mundo"/>
            <LandingCard bgColor="--color-7" icon="/assets/icons/landing-video-call.png" title="Online" text="Melhores mestres do mundo"/>
        </div>
    </div>
</section>

<section class="row">
    <header id="section-3-header">
        <span></span>
        <h1>Entra em <span>contacto</span></h1>
    </header>
    <div id="section-3-body">
        <div id="message-form">
            <h1>Não hesite em nos contactar</h1>
            <LandingInput label="Nome completo"/>
            <LandingInput label="Email"/>
            <LandingInput label="Assunto"/>
            <LandingInput large={true} label="Escreva a sua mensagem aqui"/>
        </div>
        <img src="/assets/images/landing-contact.png" alt="Woman talking on the phone">
    </div>
</section>

<style>
    :global(body){
        background-color: var(--color-8);
    }

    .row{
        width: 100%;
        height: 100%;
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
        padding-top: 5rem;
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

    #why-us-cards{
        display: grid;
        max-width: 30%;
        max-height: 25%;
        grid-template-rows: 50% 50%;
        grid-template-columns: 50% 50%;
        gap: 1rem;
    }

    .row:nth-child(3){
        padding: 2rem 0 0 2rem;
    }

    #section-3-header{
        display: flex;
        align-items: center;
        gap: 2rem;
    }

    #section-3-header h1{
        color: var(--color-6);
    }

    #section-3-header h1 span{
        color: var(--color-1);
    }

    #section-3-header > span{
        display: block;
        height: 0.125rem;
        width: 6rem; 
        background-color: var(--color-2);
    }

    #section-3-body{
        display: flex;
        justify-content: flex-start;
        align-items: flex-start;
        padding-top: 2rem;
        gap:4rem;
    }

    #message-form h1{
        font-size: 2rem;
        font-family: "Lato";
        font-weight: bold;
        margin-bottom: 2rem;
    }

    #section-3-body img{
        max-width: 45%;
        max-height: 45%;
    }

    @media(max-width: 1366px){
        .split{
            margin-top: 1rem;
        }

        #why-us-cards{
            max-width: 29%;
            max-height: 25%;
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

        #why-us-cards{
            max-width: 29%;
            max-height: 25%;
        }
    }
</style>
