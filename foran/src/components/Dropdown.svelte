<script lang="typescript">
    export let heading: string;
</script>

<div class="dropdown">
    <a href="#" aria-haspopup="true">{heading}</a>
    <ul class="dropdown-content" aria-label="submenu">
        <slot></slot>
        <li><a href="#">Central de aulas</a></li>
        <li><a href="#">Terminar sessão</a></li>
    </ul>
</div>

<style>

    .dropdown{
        position: relative;
        width: fit-content;
    }
    .dropdown > a {
        text-decoration: none;
        color: white;
    }

    .dropdown-content{
        display: none;
        min-width: fit-content;
        position: absolute;
        list-style: none;
        background-color: white;
        padding: 0.5rem;
    }

    .dropdown-content li a{
        color: black;
    }


    .dropdown:hover .dropdown-content{
        display:flex;
        padding: 0.5rem;
        flex-direction: column;
        gap: 0.5rem;
    }
</style>
