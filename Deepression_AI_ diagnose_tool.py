import shelve
import tensorflow as tf
import tkinter as tk
from sklearn.model_selection import train_test_split


def create_model():
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(50, input_shape=(15,), activation='relu')) # agregamos 15 neuronas en la capa oculta
    model.add(tf.keras.layers.Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model


def train_model(model, data, labels):
    X_train, X_val, y_train, y_val = train_test_split(data, labels, test_size=0.2, random_state=0)
    model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=50, batch_size=1)


def save_model(model):
    model.save('psychological_help_model.h5')


def load_model():
    return tf.keras.models.load_model('psychological_help_model.h5')


def get_diagnosis(model, data):
    return model.predict(data)


def diagnose(model, symptom_vars, intensity_entries):
    patient_data = []
    for symptom_var, intensity_entry in zip(symptom_vars, intensity_entries):
        if symptom_var.get():
            try:
                intensity = float(intensity_entry.get())
                if intensity >= 0 and intensity <= 10:
                    patient_data.append(intensity)
                else:
                    raise ValueError
            except ValueError:
                print('Error: la intensidad debe ser un número entre 0 y 10')
                return "Error: la intensidad debe ser un número entre 0 y 10"
        else:
            patient_data.append(0.0)
    diagnosis = get_diagnosis(model, [patient_data])
    print('Diagnosis:', diagnosis)
    return "Diagnosis: " + str(diagnosis[0][0])


def main():
    data = []
    labels = []
    db = shelve.open('psychological_help_database')
    try:
        data = db['data']
        labels = db['labels']
    except KeyError:
        print('No data found, starting from scratch')

    model = create_model()
    train_model(model, data, labels)
    save_model(model)
    db['data'] = data
    db['labels'] = labels
    db.close()

    root = tk.Tk()
    root.title("Diagnóstico de ayuda psicológica")

    # Add language selection
    label = tk.Label(root, text="Seleccione su idioma:")
    label.pack()
    language_var = tk.StringVar(value="es")
    language_options = ["Español", "English"]
    language_menu = tk.OptionMenu(root, language_var, *language_options)
    language_menu.pack()

    # Add symptom selection
    symptom_labels = ["Tristeza", "Ansiedad", "Cansancio", "Insomnio", "Irritabilidad", "Problemas de concentración", "Falta de apetito", "Pensamientos negativos", "Dolor de cabeza", "Náuseas", "Dolor muscular", "Mareos", "Sudoración excesiva", "Problemas respiratorios", "Otros"]
    symptom_vars = [tk.IntVar() for _ in symptom_labels]
    symptom_checkboxes = [tk.Checkbutton(root, text=label, variable=var) for label, var in zip(symptom_labels, symptom_vars)]
    for checkbox in symptom_checkboxes:
        checkbox.pack()

    # Add intensity entry
    intensity_labels = ["Intensidad " + label
    # Add symptom selection
    symptom_labels = ["Tristeza", "Ansiedad", "Cansancio", "Insomnio", "Irritabilidad", "Problemas de concentración", "Falta de apetito", "Pensamientos negativos", "Dolor de cabeza", "Náuseas", "Dolor muscular", "Malestar estomacal"]
    symptom_vars = []
    intensity_entries = []
    symptom_frame = tk.Frame(root)
    symptom_frame.pack()
    for label_text in symptom_labels:
        var = tk.BooleanVar()
        symptom_vars.append(var)
        checkbutton = tk.Checkbutton(symptom_frame, text=label_text, variable=var)
        checkbutton.pack(side=tk.LEFT, padx=5, pady=5)
        intensity_entry = tk.Entry(symptom_frame, width=5)
        intensity_entries.append(intensity_entry)
        intensity_entry.pack(side=tk.LEFT, padx=5, pady=5)

    # Add diagnose button
    diagnose_button = tk.Button(root, text="Diagnóstico", command=lambda: diagnose(model, symptom_vars, intensity_entries))
    diagnose_button.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
    