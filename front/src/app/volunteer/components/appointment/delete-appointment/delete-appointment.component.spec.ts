import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DeleteAppointmentComponent } from './delete-appointment.component';

describe('DeleteAppointmentComponent', () => {
  let component: DeleteAppointmentComponent;
  let fixture: ComponentFixture<DeleteAppointmentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DeleteAppointmentComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DeleteAppointmentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
