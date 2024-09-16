<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import { onMount } from 'svelte';

	interface ApiResponse {
		message: string;
	}

	let responseData: ApiResponse;
	let message: string | undefined;

	onMount(async () => {
		try {
			const response = await fetch('/api/');
			if (response.ok) {
				responseData = await response.json();
				message = responseData.message; // Access the 'message' from the JSON body
			} else {
				console.error(`Error: ${response.status} - ${response.statusText}`);
			}
		} catch (error) {
			console.error('Error fetching API:', error);
		}
	});
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
<Button>Click me</Button>
<p>{message}</p>
