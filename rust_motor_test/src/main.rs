use rppal::gpio::{Gpio, Level};
use std::thread;
use std::time::Duration;

fn main() {
    let gpio = Gpio::new().unwrap();
    
    let mut led = gpio.get(18).unwrap().into_output();
    
    loop {
        println!("On");
        led.write(Level::High);
        thread::sleep(Duration::from_millis(5000));
    
        println!("Off");
        led.write(Level::Low);
        thread::sleep(Duration::from_millis(5000));
    }
}