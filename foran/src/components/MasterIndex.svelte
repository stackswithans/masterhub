<script lang="typescript">
    export let name = "Maria";
    export let classes = "Chemistry";
</script>

<div class="main">
    <div class="media">
        <div class="photo">
            <img src="" alt="">
        </div>
        <div class="edit">Editar foto</div>
    </div>
    <div class="id-div">
        <div class="identification">
            <h1>{name}</h1>
            <h2>{classes}</h2>
        </div>
    </div>
    <div class="info">
        <div>Informações pessoais</div>
        <div>Agenda</div>
        <div>Contactos</div>
        <div>Aulas</div>
    </div>
</div>



<style>
    .main{
        display: flex;
        width: 55vw;
        height: 30vh;
        background-color: var(--color-3);
        border-radius: 20px;
    }

    .media{
        width: 8vw;
        height:16vh;
        margin: auto 0rem;
        margin-left: 4rem;
    }

    .photo{
        width: 8vw;
        height: 8vw;
        border-radius: 100px;
        border: 1px solid black;
    }

    .edit{
        padding: 0.8rem 1.8rem;
        font-family: 'Roboto';
        font-size: 1rem;
        color: white;
        font-weight: lighter;
    }

    .id-div{
        width: 18vw;
        height: 8vh;
        margin: auto 0rem;
        padding-left: 1rem;
    }

    .identification h1{
        font-family: 'Roboto';
        font-weight: bold;
        font-size: 2.2rem;
        color: var(--color-7);
    }

    .identification h2{
        font-family: 'Roboto';
        font-weight: normal;
        font-size: 1.6rem;
        color: var(--color-7);
    }

    .info{
        display: flex;
        color: var(--color-7);
        font-size: 1rem;
        font-family: 'Roboto Regular';
        margin-top: 13rem;
    }

    .info div{
        padding: 0.6rem;
    }

</style>