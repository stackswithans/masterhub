<script lang="typescript">
    import ContactCircle from "./ContactCircle.svelte";

    export let name = "Migue Voa";
    export let surname = "Voa";
    export let course = "IT";
    export let phone = "945415191";
    export let gender = "Masculino";
    export let location = "Grafanil-Viana";
    export let graduation = "Licenciado- Eng. informática";
    export let work = "XPTO- Eng. Auxiliar";
    export let subject = "Electrónica, Mecânica";
</script>

    <div class="container">
        <div class="first">
            <div class="image">
                <ContactCircle  size="4em"/>
            </div>
            <h2>{name} {surname}</h2>
            <h2 class="course">{course}</h2>
            <h5>x classificações</h5>
        </div>
        <div class="second">
            <div class="sobre">
                <h3>Sobre</h3>
            </div>
        </div>
        <div class="third">
            <div class="skills-list">
                <h3><i class="fas fa-phone-alt"></i>{phone}</h3>
                <h3><i class="fas fa-venus-mars"></i>{gender}</h3>
                <h3><i class="fas fa-map-marker-alt"></i>{location}</h3>
                <h3><i class="fas fa-graduation-cap"></i>{graduation}</h3>
                <h3><i class="fas fa-briefcase"></i>{work}</h3>
                <h3><i class="fas fa-book"></i>{subject}</h3>
            </div>
        </div>
    </div>

<style>

    .container{
        display: flex;
        flex-direction: column;
        width: min(80%, 16.652375em);
        height: fit-content;
        border-radius: 15px;
        border: 0px solid black;
        box-shadow: 0rem 0rem 0.3rem;
        padding: 1em;
        background-color: white;
    }

    .first{
        width: 100%;
        height: 32%;
        display: flex;
        flex-direction: column;
        gap: 0.5em;
    }

    .container h2{
        text-align: center;
        font-size: 1.2em;
        font-family: 'Roboto';
        font-weight: normal;
    }

    .container .first .course{
        font-weight: bold;
    }

    .container h5{
        text-align: center;
        opacity: 0.7;
    }

    .second{
        width: 100%;
        height: 5%;
        display: flex;
        margin-top: 5%;
    }

    .sobre{
        display: flex;
        width: 20%;
        margin: auto;
        border-bottom: 3px solid var(--color-3);
        justify-content: center;
    }

    .sobre h3{
        font-family: 'Roboto Slab';
        font-size: 1em;
    }

    .image{
        margin: auto;
    }

    .third{
        width: 100%;
        height: 63%;
        display: flex;
    }

    .skills-list{
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        gap: 2rem;
        padding: 2em 0.5em 0 1em;
    }

    .skills-list h3{
        display: flex;
        gap: 1.5rem;
        align-items: center;
        padding: 0 0 0 4%;
        color: var(--color-3);
        opacity: 0.7;
        font-size: 0.8em;
    }

</style>
