import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InspectProfessionalComponent } from './inspect-professional.component';

describe('InspectProfessionalComponent', () => {
  let component: InspectProfessionalComponent;
  let fixture: ComponentFixture<InspectProfessionalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InspectProfessionalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InspectProfessionalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
