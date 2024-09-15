const API_URL = 'http://localhost:5000';

export const uploadDocument = async (file) => {
    const formData = new FormData();
    formData.append('file',file);

    try {
        const response = await fetch(`${API_URL}/upload`, {
            method: 'POST',
            body: formData,
        });
        
        console.log('Raw response: ', response);

        if (!response.ok) {
            const errorResponse = await response.json();
            console.log('Error response:', errorResponse);
            return {error: errorResponse.error || 'Upload failed'};
        }

        const successResponse = await response.json();
        console.log('Success response:', successResponse);  // Log the success response
        return successResponse;
        
    } catch (error) {
        console.error('Error uploading file:', error);
        return { error: 'Upload failed'};
    }
};