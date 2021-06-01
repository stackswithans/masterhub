<script lang="typescript">
    import LandingCard from "./LandingCard.svelte";
</script>


<div>
    <LandingCard bColor="--color-2" icon="/assets/icons/landing-class.png" title="Tutores" text="Altamente qualificados e prontos a ensinar"/>
    <LandingCard bColor="--color-6" icon="/assets/icons/landing-idea.png" title="Estratégia" text="Totalmente adaptada ao contexto nacional"/>
    <LandingCard bColor="--color-6" icon="/assets/icons/landing-cog.png" title="Fácil" text="Plataforma intuitiva e de fácil acesso"/>
    <LandingCard bgColor="--color-7" icon="/assets/icons/landing-video-call.png" title="Online" text="Ensino totalmente online"/>
</div>

<style>
    div{
        display: grid;
        max-width: 30%;
        max-height: 25%;
        grid-template-rows: 1fr 1fr;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
    }

    @media(max-width: 1366px){
        div{
            max-width: 29%;
            max-height: 25%;
        }
    }

</style>
