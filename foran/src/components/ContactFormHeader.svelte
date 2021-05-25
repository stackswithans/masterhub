<header>
    <div class="header">
        <span></span>
        <h1>Entra em <span>contacto</span></h1>
    </div>
    <h1>Não hesite em nos contactar</h1>
</header>

<style>
    header{
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 3rem;
    }

    .header{
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .header h1{
        color: var(--color-6);
    }

    .header h1 > span{
        color: var(--color-1);
    }

    .header > span{
        height: 0.125rem;
        width: 6rem; 
        background-color: var(--color-2);
    }

    header > h1{
        font-size: 2rem;
        font-family: "Lato";
        font-weight: bold;
        margin-bottom: 2rem;
    }
</style>
