<script lang="typescript">
    import LandingCard from "./LandingCard.svelte";
</script>


<div>
    <LandingCard bColor="--color-2" icon="/assets/icons/landing-class.png" title="Professores" text="Melhores mestres do mundo"/>
    <LandingCard bColor="--color-6" icon="/assets/icons/landing-idea.png" title="Estratégia" text="Melhores mestres do mundo"/>
    <LandingCard bColor="--color-6" icon="/assets/icons/landing-cog.png" title="Fácil" text="Melhores mestres do mundo"/>
    <LandingCard bgColor="--color-7" icon="/assets/icons/landing-video-call.png" title="Online" text="Melhores mestres do mundo"/>
</div>

<style>
    div{
        display: grid;
        max-width: 30%;
        max-height: 25%;
        grid-template-rows: 50% 50%;
        grid-template-columns: 50% 50%;
        gap: 1rem;
    }

    @media(max-width: 1366px){
        div{
            max-width: 29%;
            max-height: 25%;
        }
    }

</style>
