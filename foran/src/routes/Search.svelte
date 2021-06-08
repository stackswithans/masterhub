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
        margin-top: -14rem;
    }

    .container h1{
        text-align: center;
        color: var(--color-4);
        font-family: 'Roboto Condensed';
        font-size: 4.7rem;
        font-weight: lighter;
    }

    .container h3{
        text-align: center;
        color: var(--color-4);
        font-family: 'Roboto Condensed';
        font-size: 1.7rem;
        font-weight: lighter;
        opacity: 0.75;
        padding: 1rem;
    }

    .bar{
        max-width: 45rem;
        margin-left: 10rem;
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
        text-indent: 14rem;
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