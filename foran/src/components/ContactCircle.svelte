
<script lang="typescript">
    export let initials = "TS";
    export let size = "3.2em";
    export let fontSize = "1em";
</script>

<div>
    <div style="height:{size};width:{size};font-size:{fontSize};" class="circle">{initials.toUpperCase()}</div>
</div>


<style>
    .circle{
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: var(--color-2);
        border-radius: 40px;
        font-weight: bold;
    }
</style>
