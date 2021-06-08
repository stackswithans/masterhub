
<script lang="typescript">
    export let visible: boolean;
</script>

<div style="display: {(visible)?'block':'none'}" class="form-section">
    <slot></slot>
</div>
