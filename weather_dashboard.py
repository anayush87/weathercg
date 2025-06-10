import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime

class WeatherDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Dashboard - Color & Lighting Models")
        self.root.geometry("700x500")
        self.root.configure(bg='#74b9ff')
        
        # Weather data
        self.weather_data = {
            'temperature': 24,
            'condition': 'Sunny',
            'humidity': 65,
            'wind_speed': 12,
            'pressure': 1013,
            'location': 'New Delhi, India'
        }
        
        # Color schemes for different weather conditions
        self.color_schemes = {
            'Sunny': {'bg': '#fdcb6e', 'fg': '#2d3436', 'accent': '#e17055'},
            'Cloudy': {'bg': '#636e72', 'fg': '#ffffff', 'accent': '#74b9ff'},
            'Rainy': {'bg': '#74b9ff', 'fg': '#ffffff', 'accent': '#0984e3'},
            'Snowy': {'bg': '#ddd', 'fg': '#2d3436', 'accent': '#636e72'}
        }
        
        self.setup_ui()
        self.update_weather_display()
        
    def setup_ui(self):
        # Main container
        main_frame = tk.Frame(self.root, bg='#74b9ff')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(main_frame, text="Weather Dashboard", 
                              font=('Arial', 20, 'bold'), 
                              bg='#74b9ff', fg='white')
        title_label.pack(pady=(0, 15))
        
        # Current weather card
        self.weather_card = tk.Frame(main_frame, bg='white', relief='raised', bd=3)
        self.weather_card.pack(fill='x', pady=(0, 15))
        
        # Weather info container
        weather_info = tk.Frame(self.weather_card, bg='white')
        weather_info.pack(fill='x', padx=20, pady=20)
        
        # Temperature and condition
        self.temp_label = tk.Label(weather_info, text="24°C", 
                                  font=('Arial', 36, 'bold'), 
                                  bg='white', fg='#0984e3')
        self.temp_label.pack()
        
        self.condition_label = tk.Label(weather_info, text="Sunny", 
                                       font=('Arial', 16), 
                                       bg='white', fg='#636e72')
        self.condition_label.pack(pady=(5, 0))
        
        self.location_label = tk.Label(weather_info, text="New Delhi, India", 
                                      font=('Arial', 12), 
                                      bg='white', fg='#74b9ff')
        self.location_label.pack(pady=(5, 15))
        
        # Weather details grid
        self.details_frame = tk.Frame(weather_info, bg='white')
        self.details_frame.pack(fill='x')
        self.create_details_grid()
        
        # Forecast section
        forecast_frame = tk.Frame(main_frame, bg='white', relief='raised', bd=3)
        forecast_frame.pack(fill='both', expand=True, pady=(0, 15))
        
        forecast_title = tk.Label(forecast_frame, text="5-Day Forecast", 
                                 font=('Arial', 14, 'bold'), 
                                 bg='white', fg='#2d3436')
        forecast_title.pack(pady=(10, 5))
        
        self.create_forecast_section(forecast_frame)
        
        # Color model demonstration
        color_demo_frame = tk.Frame(main_frame, bg='white', relief='raised', bd=3)
        color_demo_frame.pack(fill='x', pady=(0, 15))
        self.create_color_demo(color_demo_frame)
        
        # Control buttons
        button_frame = tk.Frame(main_frame, bg='#74b9ff')
        button_frame.pack(fill='x')
        
        refresh_btn = tk.Button(button_frame, text="Refresh Data", 
                               command=self.refresh_weather,
                               font=('Arial', 10, 'bold'),
                               bg='#0984e3', fg='white', relief='raised')
        refresh_btn.pack(side='left', padx=(0, 10))
        
        theme_btn = tk.Button(button_frame, text="Change Theme", 
                             command=self.change_theme,
                             font=('Arial', 10, 'bold'),
                             bg='#e17055', fg='white', relief='raised')
        theme_btn.pack(side='left')
    
    def create_details_grid(self):
        # Clear existing details
        for widget in self.details_frame.winfo_children():
            widget.destroy()
            
        details = [
            ("Humidity", f"{self.weather_data['humidity']}%"),
            ("Wind", f"{self.weather_data['wind_speed']} km/h"),
            ("Pressure", f"{self.weather_data['pressure']} hPa"),
            ("Condition", self.weather_data['condition'])
        ]
        
        for i, (label, value) in enumerate(details):
            row = i // 2
            col = i % 2
            
            detail_card = tk.Frame(self.details_frame, bg='#f8f9fa', relief='raised', bd=1)
            detail_card.grid(row=row, column=col, padx=5, pady=5, sticky='ew')
            
            self.details_frame.grid_columnconfigure(col, weight=1)
            
            tk.Label(detail_card, text=label, font=('Arial', 9), 
                    bg='#f8f9fa', fg='#636e72').pack(pady=(8, 2))
            tk.Label(detail_card, text=value, font=('Arial', 11, 'bold'), 
                    bg='#f8f9fa', fg='#2d3436').pack(pady=(0, 8))
    
    def create_forecast_section(self, parent):
        forecast_container = tk.Frame(parent, bg='white')
        forecast_container.pack(fill='x', padx=15, pady=(0, 15))
        
        # Sample forecast data with weather icons
        forecast_data = [
            ("Today", "☀️", "24°"),
            ("Tue", "⛅", "22°"),
            ("Wed", "🌧️", "19°"),
            ("Thu", "⛈️", "21°"),
            ("Fri", "☀️", "26°")
        ]
        
        for i, (day, icon, temp) in enumerate(forecast_data):
            card = tk.Frame(forecast_container, bg='#f1f3f4', relief='raised', bd=1)
            card.grid(row=0, column=i, padx=3, pady=5, sticky='ew')
            
            forecast_container.grid_columnconfigure(i, weight=1)
            
            tk.Label(card, text=day, font=('Arial', 9, 'bold'), 
                    bg='#f1f3f4', fg='#2d3436').pack(pady=(8, 2))
            tk.Label(card, text=icon, font=('Arial', 16), 
                    bg='#f1f3f4').pack(pady=2)
            tk.Label(card, text=temp, font=('Arial', 10, 'bold'), 
                    bg='#f1f3f4', fg='#0984e3').pack(pady=(2, 8))
    
    def create_color_demo(self, parent):
        tk.Label(parent, text="Weather Color Models", 
                font=('Arial', 12, 'bold'), 
                bg='white', fg='#2d3436').pack(pady=(10, 5))
        
        color_container = tk.Frame(parent, bg='white')
        color_container.pack(pady=(0, 10))
        
        colors = [
            ("Sunny", "#fdcb6e"),
            ("Cloudy", "#636e72"),
            ("Rainy", "#74b9ff"),
            ("Snowy", "#ddd"),
            ("Stormy", "#2d3436"),
            ("Windy", "#00b894"),
            ("Foggy", "#b2bec3"),
            ("Hot", "#e17055")
        ]
        
        for i, (name, color) in enumerate(colors):
            color_swatch = tk.Frame(color_container, bg=color, width=60, height=60, 
                                   relief='raised', bd=2)
            color_swatch.grid(row=0, column=i, padx=8, pady=5)
            color_swatch.grid_propagate(False)
            
            text_color = 'black' if color == "#ddd" else 'white'
            tk.Label(color_swatch, text=name, font=('Arial', 8, 'bold'), 
                    bg=color, fg=text_color).pack(expand=True)
    
    def update_weather_display(self):
        # Update main display
        self.temp_label.config(text=f"{self.weather_data['temperature']}°C")
        self.condition_label.config(text=self.weather_data['condition'])
        self.location_label.config(text=self.weather_data['location'])
        
        # Apply color scheme based on weather condition
        condition = self.weather_data['condition']
        if condition in self.color_schemes:
            scheme = self.color_schemes[condition]
            
            # Update weather card background
            self.weather_card.config(bg=scheme['bg'])
            
            # Update all child widgets in weather card
            self.update_widget_colors(self.weather_card, scheme['bg'], scheme['fg'])
        
        # Refresh details grid
        self.create_details_grid()
    
    def update_widget_colors(self, widget, bg_color, fg_color):
        try:
            if isinstance(widget, (tk.Label, tk.Frame)):
                widget.config(bg=bg_color)
                if isinstance(widget, tk.Label):
                    widget.config(fg=fg_color)
        except:
            pass
        
        # Update child widgets
        for child in widget.winfo_children():
            self.update_widget_colors(child, bg_color, fg_color)
    
    def refresh_weather(self):
        # Simulate new weather data
        conditions = ['Sunny', 'Cloudy', 'Rainy', 'Snowy']
        self.weather_data.update({
            'condition': random.choice(conditions),
            'temperature': random.randint(15, 50),
            'humidity': random.randint(40, 85),
            'wind_speed': random.randint(5, 25),
            'pressure': random.randint(995, 1025)
        })
        
        self.update_weather_display()
        print(f"Weather updated: {self.weather_data['condition']}, {self.weather_data['temperature']}°C")
    
    def change_theme(self):
        # Cycle through background themes
        themes = ['#74b9ff', '#6c5ce7', '#a29bfe', "#000000", "#000000"]
        current_bg = self.root.cget('bg')
        
        try:
            current_index = themes.index(current_bg)
            new_theme = themes[(current_index + 1) % len(themes)]
        except ValueError:
            new_theme = themes[0]
        
        self.root.config(bg=new_theme)
        
        # Update main frame
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.config(bg=new_theme)
                self.update_main_theme(widget, new_theme)
    
    def update_main_theme(self, widget, theme_color):
        for child in widget.winfo_children():
            if isinstance(child, tk.Label) and 'Arial' in str(child.cget('font')):
                if child.cget('fg') == 'white':
                    child.config(bg=theme_color)
            elif isinstance(child, tk.Frame) and child.cget('bg') != 'white':
                child.config(bg=theme_color)
                self.update_main_theme(child, theme_color)

def main():
    root = tk.Tk()
    app = WeatherDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()