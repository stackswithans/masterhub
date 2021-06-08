<script lang="typescript">
    export let phone = "945415191";
    export let gender = "Masculino";
    export let location = "Grafanil-Viana";
    export let graduation = "Licenciado- Eng. informática";
    export let work = "XPTO- Eng. Auxiliar";
    export let subject = "Electrónica, Mecânica";
</script>

    <div class="container">
        <div class="image-container">
            <div class="image">
                <img src="" alt="">
            </div>
        </div>
        <h2>Tony Stark</h2>
        <h2>INFORMÁTICA</h2>
        <h4>x classificações</h4>
        <div class="h3-div">
            <h3>Sobre</h3>
        </div>
        <div class="skills-list">
            <h3><i class="fas fa-phone-alt"></i>{phone}</h3>
            <h3><i class="fas fa-venus-mars"></i>{gender}</h3>
            <h3><i class="fas fa-map-marker-alt"></i>{location}</h3>
            <h3><i class="fas fa-graduation-cap"></i>{graduation}</h3>
            <h3><i class="fas fa-briefcase"></i>{work}</h3>
            <h3><i class="fas fa-book"></i>{subject}</h3>
        </div>
    </div>

<style>

    .container{
        width: 20vw;
        height: 70vh;
        border-radius: 15px;
        border: 0px solid black;
        box-shadow: 0rem 0rem 0.5rem;
        padding: 1rem;
        background-color: white;
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

    .h3-div h3{
        text-align: center;
        padding: 0rem;
        font-family: 'Roboto Slab';
        font-size: 1.2rem;
    }

    .h3-div{
        width: 5rem;
        border-bottom: 2px solid var(--color-3);
        margin: auto;
    }

    .skills-list{
        width: 20vw;
        height: 45vh;
        padding: 2rem 0rem;
    }

    .skills-list h3{
        padding: 1rem 0rem;
        font-family: 'Roboto Condensed';
        font-size: 1.2rem;
        color: var(--color-3);
        opacity: 0.5;
    }

    .skills-list i{
        padding: 0rem 1.5rem;
    }

    .image{
        margin: auto;
        width: 5rem;
        height: 5rem;
        border: 1px solid  black;
        border-radius: 40px;
    }

    .image-container{
        position: relative;
        width: 100%;
        height: 5rem;
    }

</style>