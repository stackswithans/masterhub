<script lang="typescript">
    export let name = "Migue Voa";
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
                <img src="" alt="">
            </div>
            <h2>{name}</h2>
            <h2>{course}</h2>
            <h4>x classificações</h4>
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
        width: 80%;
        height: 80%;
        border-radius: 15px;
        border: 0px solid black;
        box-shadow: 0rem 0rem 0.3rem;
        padding: 1rem 1rem 0 1rem;
        background-color: white;
        display: flex;
        flex-direction: column;
    }

    .first{
        width: 100%;
        height: 32%;
        display: flex;
        flex-direction: column;
    }

    .container h2{
        text-align: center;
        padding: 0.5rem;
        font-size: 1.6rem;
        font-family: 'Roboto';
    }

    .container h4{
        text-align: center;
        padding: 0.5rem;
        opacity: 0.7;
    }

    .second{
        width: 100%;
        height: 5%;
        display: flex;
        padding: 1rem;
    }

    .sobre{
        display: flex;
        width: 20%;
        justify-content: center;
        margin: auto;
        border-bottom: 3px solid var(--color-3);
    }

    .sobre h3{
        font-family: 'Roboto Slab';
        font-size: 1.2rem;
    }

    .image{
        margin: auto;
        width: 90px;
        height: 100%;
        border: 1px solid  black;
        border-radius: 100px;
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
        padding-top: 2rem;
    }

    .skills-list h3{
        display: flex;
        gap: 1.5rem;
        align-items: center;
        padding: 0 0 0 4%;
        color: var(--color-3);
        opacity: 0.7;
    }



</style>