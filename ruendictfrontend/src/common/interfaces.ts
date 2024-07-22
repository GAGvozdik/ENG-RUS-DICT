// interfaces.ts

export interface SelectInterface {
    en: string; 
    rus: number;
}

export interface ComboBoxProps {
    words: SelectInterface[];
    width?: number | string; // Добавляем опциональное свойство width
}

