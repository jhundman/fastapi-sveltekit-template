import type { RequestHandler } from './$types';
import { PUBLIC_BACKEND_PATH } from '$env/static/public';

const handler: RequestHandler = async ({ params, url, request }) => {
	const response = await fetch(`${PUBLIC_BACKEND_PATH}/${params.path ?? ''}${url.search}`, {
		method: request.method,
		headers: request.headers,
		body: request.method !== 'GET' && request.method !== 'HEAD' ? await request.text() : undefined
	});

	return response;
};

export const GET = handler;
export const POST = handler;
export const PUT = handler;
export const PATCH = handler;
export const DELETE = handler;
