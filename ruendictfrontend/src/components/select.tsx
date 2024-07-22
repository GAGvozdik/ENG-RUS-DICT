import React from 'react';
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';
import { ComboBoxProps } from '../common/interfaces';


const ComboBox: React.FC<ComboBoxProps> = ({ words, width }) => {
    return (
        <Autocomplete
            disablePortal
            id="combo-box-demo"
            options={words.map((option) => option.en)} // Пример: отображаем только en или адаптируйте под ваши нужды
            sx={{ width: width }}
            renderInput={(params) => <TextField {...params} label="Movie" />}
        />
    );
}

export default ComboBox;
