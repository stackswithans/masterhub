<script lang="typescript">
    import MainLayout from "../components/MainLayout.svelte";
</script>

    <MainLayout>
        <div class="container">
            <h1>Conhecimento à medida</h1>
            <h3>Mais de x cursos em áreas que vão de cultura à tecnologias, com os tutores mais qualificados</h3>
            <div class="bar">
                <input type="text" placeholder="Pesquise pela habilidade que deseja">
                <i class="fas fa-search"></i>
            </div>
        </div>
    </MainLayout>

<style>
    .container{
        display: flex;
        padding-top: 10em;
        flex-direction: column;
        align-items: center;
        width: 100%;
        height: 100%;
    }

    .container h1{
        text-align: center;
        color: var(--color-4);
        font-family: 'Roboto Condensed';
        font-size: 2.5em;
        font-weight: lighter;
    }

    .container h3{
        text-align: center;
        color: var(--color-4);
        font-family: 'Roboto Condensed';
        font-size: 1.5em;
        font-weight: normal;
        opacity: 0.75;
        padding: 1rem;
    }

    .bar{
        display:flex;
        padding:0.4em;
        width: min(30em, 45%);
        background-color: var(--color-4);
        border-radius: 20px;
        border: 0px solid black;
    }

    .bar input{
        margin: auto;
        border: 0px solid black;
        border-radius: 20px;
        background-color: var(--color-4);
        position: relative;
        width: 95%;
        text-indent: 4ch;
    }

    .bar input:focus{
        outline: none;
    }

    .bar input::placeholder{
        opacity: 0.35;
    }

    .fa-search{
        color: white;
        background-color: black;
        border-radius: 25px;
        padding: 0.4rem;
    }
</style>
