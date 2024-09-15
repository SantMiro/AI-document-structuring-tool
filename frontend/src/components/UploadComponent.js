import React, { useState } from 'react';
import { uploadDocument } from '../services/api';

const UploadComponent = () => {
    const [file, setFile] = useState(null);
    const [message, setMessage] = useState('');
    
    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!file) {
            setMessage('Please select a file');
            return;
        }

        const response = await uploadDocument(file);
        setMessage(response.message || response.error); 
    };

    return (
        <div>
            <h2>upload Document</h2>
            <form onSubmit={handleSubmit}>
                <input type='file' onChange={handleFileChange} />
                <button type='submit'>Upload</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default UploadComponent;
