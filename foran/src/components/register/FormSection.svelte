
<script lang="typescript">
    export let currentStep: number;
    export let sectionStep: number;
</script>

<div style="display: {(currentStep == sectionStep)?'block':'none'}" class="form-section">
    <slot></slot>
</div>
