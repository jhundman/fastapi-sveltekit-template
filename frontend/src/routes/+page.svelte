<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import { Input } from '$lib/components/ui/input/index.js';
	// import * as Card from '$lib/components/ui/card/index.js';
	// import { Checkbox } from '$lib/components/ui/checkbox';
	import { onMount } from 'svelte';

	interface Todo {
		id: string;
		task: string;
		is_completed: boolean;
		created_at: string;
		updated_at: string;
	}

	interface ApiResponse {
		message: string;
		todos?: Todo[];
	}

	let responseData: ApiResponse;
	let message: string | undefined;
	let todos: Todo[] = [];
	let newTask: string = '';

	// Fetch data from the API on component mount
	onMount(async () => {
		try {
			const response = await fetch('/api/todos');
			if (response.ok) {
				responseData = await response.json();
				console.log(responseData);
				todos = responseData.todos || [];
				message = responseData.message;
			} else {
				console.error(`Error: ${response.status} - ${response.statusText}`);
			}
		} catch (error) {
			console.error('Error fetching API:', error);
		}
	});

	// Create a new task
	async function addTodo() {
		if (newTask.trim() === '') return;
		try {
			const response = await fetch('/api/todos', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({ task: newTask, is_completed: false })
			});
			if (response.ok) {
				const newTodo = await response.json();
				todos = [...todos, newTodo];
				newTask = '';
			} else {
				console.error(`Error: ${response.status} - ${response.statusText}`);
			}
		} catch (error) {
			console.error('Error adding new task:', error);
		}
	}

	// Toggle the completion status of a task
	async function toggleTodoCompletion(todo: Todo) {
		try {
			const response = await fetch(`/api/todos/${todo.id}`, {
				method: 'PUT',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({ task: todo.task, is_completed: !todo.is_completed })
			});
			if (response.ok) {
				todos = todos.map((t) => (t.id === todo.id ? { ...t, is_completed: !t.is_completed } : t));
			} else {
				console.error(`Error: ${response.status} - ${response.statusText}`);
			}
		} catch (error) {
			console.error('Error updating task:', error);
		}
	}

	// Delete a task
	async function deleteTodo(id: string) {
		try {
			const response = await fetch(`/api/todos/${id}`, {
				method: 'DELETE'
			});
			if (response.ok) {
				todos = todos.filter((todo) => todo.id !== id);
			} else {
				console.error(`Error: ${response.status} - ${response.statusText}`);
			}
		} catch (error) {
			console.error('Error deleting task:', error);
		}
	}
</script>

<div class="mx-auto flex min-h-[95dvh] max-w-screen-lg flex-col px-6 space-y-6 py-2">
	<h1 class="text-center text-2xl font-bold">Welcome to Fastapi & Sveltekit Template</h1>

	<div class="flex space-x-4">
		<Input type="text" bind:value={newTask} placeholder="New task..." />
		<Button on:click={addTodo}>Add Task</Button>
	</div>

	{#if message}
		<p class="text-center">{message}</p>
	{/if}

	<ul class="py-4 space-y-2">
		{#each todos as todo}
			<li class="p-2 bg-gray-100 jus rounded-md">
				<div class="flex justify-between items-center">
					<div class="flex items-center space-x-4">
						<input
							type="checkbox"
							checked={todo.is_completed}
							on:change={() => toggleTodoCompletion(todo)}
						/>
						<span>{todo.task}</span>
					</div>
					<Button on:click={() => deleteTodo(todo.id)} variant="destructive">Delete</Button>
				</div>
			</li>
		{/each}
	</ul>
</div>
